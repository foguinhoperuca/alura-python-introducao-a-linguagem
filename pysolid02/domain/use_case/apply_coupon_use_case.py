from decimal import Decimal
from typing import Dict, Self

from domain.entities import Cart
from domain.factories import CouponType, StrategyCouponFactory
from domain.service import ApplyCouponStrategy


class ApplyCouponUseCase:
    def execute(self: Self, cart: Cart, coupon_type: CouponType) -> Dict:
        subtotal: Decimal = cart.subtotal
        discount: Decimal = ApplyCouponStrategy(strategy=StrategyCouponFactory.create(coupon_type=coupon_type)).apply_discount(value=subtotal)

        return {
            'cart_id': cart.cart_id,
            'original_subtotal': subtotal,
            'discount_value': discount,
            'discounted_price': (subtotal - discount)
        }
