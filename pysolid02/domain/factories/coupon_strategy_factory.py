from enum import auto, Enum
from typing import Dict

from domain.service.coupon import CuponStrategy, BlackFridayCoupon, ChristmasCoupon, MothersDayCoupon, FathersDayCoupon, ChildsDayCoupon


class CouponType(Enum):
    BLACK_FRIDAY = auto()
    CHRISTMAS = auto()
    MOTHERS_DAY = auto()
    FATHERS_DAY = auto()
    CHILDS_DAY = auto()


class StrategyCouponFactory:
    _STRATEGY_MAP: Dict = {
        CouponType.BLACK_FRIDAY: BlackFridayCoupon(),
        CouponType.CHRISTMAS: ChristmasCoupon(),
        CouponType.MOTHERS_DAY: MothersDayCoupon(),
        CouponType.FATHERS_DAY: FathersDayCoupon(),
        CouponType.CHILDS_DAY: ChildsDayCoupon(),
    }

    @classmethod
    def create(cls, coupon_type: CouponType) -> CuponStrategy:
        try:
            return cls._STRATEGY_MAP[coupon_type]
        except KeyError as e:
            raise ValueError(f'Type {coupon_type} not a valid strategy :: {e}')
