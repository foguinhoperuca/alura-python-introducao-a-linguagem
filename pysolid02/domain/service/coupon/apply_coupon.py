from decimal import Decimal
from typing import Self

from domain.service.coupon.coupon_strategy import CouponStrategy


class ApplyCouponStrategy:
    def __init__(self: Self, strategy: CouponStrategy) -> None:
        self._strategy: CouponStrategy = strategy

    def update(self: Self, new_strategy: CouponStrategy) -> None:
        self._strategy = new_strategy

    def apply_discount(self: Self, value: Decimal) -> Decimal:
        assert value > round(Decimal('0.00'), 2)

        return self._strategy.apply_discount(value=value)
