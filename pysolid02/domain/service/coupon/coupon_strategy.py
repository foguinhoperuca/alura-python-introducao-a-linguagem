from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Self


class CouponStrategy(ABC):
    @abstractmethod
    def apply_discount(self: Self, value: Decimal) -> Decimal:
        ...


class BaseCoupon(CouponStrategy):
    def __init__(self: Self, discount_rate: Decimal, discount_threshold_trigger: Decimal) -> None:
        assert discount_rate > round(Decimal('0.00'), 2)
        assert discount_threshold_trigger > round(Decimal('0.00'), 2)

        self._discount_rate: Decimal = discount_rate
        self._discount_threshold_trigger: Decimal = discount_threshold_trigger

    def apply_discount(self: Self, value: Decimal) -> Decimal:
        return round((value * self._discount_rate), 2) if value >= self._discount_threshold_trigger else Decimal('0.00')


class BlackFridayCoupon(BaseCoupon):
    DISCOUNT_RATE: Decimal = round(Decimal('0.2'), 2)
    DISCOUNT_THRESHOLD_TRIGGER: Decimal = round(Decimal('300.00'), 2)

    def __init__(self: Self) -> None:
        super().__init__(BlackFridayCoupon, discount_rate=BlackFridayCoupon.DISCOUNT_RATE, discount_threshold_trigger=BlackFridayCoupon.DISCOUNT_THRESHOLD_TRIGGER)


class ChristmasCoupon(BaseCoupon):
    DISCOUNT_RATE: Decimal = round(Decimal('0.3'), 2)
    DISCOUNT_THRESHOLD_TRIGGER: Decimal = round(Decimal('800.00'), 2)

    def __init__(self: Self) -> None:
        super().__init__(ChristmasCoupon, discount_rate=ChristmasCoupon.DISCOUNT_RATE, discount_threshold_trigger=ChristmasCoupon.DISCOUNT_THRESHOLD_TRIGGER)


class MothersDayCoupon(BaseCoupon):
    DISCOUNT_RATE: Decimal = round(Decimal('0.15'), 2)
    DISCOUNT_THRESHOLD_TRIGGER: Decimal = round(Decimal('500.00'), 2)

    def __init__(self: Self) -> None:
        super().__init__(MothersDayCoupon, discount_rate=MothersDayCoupon.DISCOUNT_RATE, discount_threshold_trigger=MothersDayCoupon.DISCOUNT_THRESHOLD_TRIGGER)


class FathersDayCoupon(BaseCoupon):
    DISCOUNT_RATE: Decimal = round(Decimal('0.25'), 2)
    DISCOUNT_THRESHOLD_TRIGGER: Decimal = round(Decimal('1000.00'), 2)

    def __init__(self: Self) -> None:
        super().__init__(FathersDayCoupon, discount_rate=FathersDayCoupon.DISCOUNT_RATE, discount_threshold_trigger=FathersDayCoupon.DISCOUNT_THRESHOLD_TRIGGER)


class ChildsDayCoupon(BaseCoupon):
    DISCOUNT_RATE: Decimal = round(Decimal('0.10'), 2)
    DISCOUNT_THRESHOLD_TRIGGER: Decimal = round(Decimal('450.00'), 2)

    def __init__(self: Self) -> None:
        super().__init__(ChildsDayCoupon, discount_rate=ChildsDayCoupon.DISCOUNT_RATE, discount_threshold_trigger=ChildsDayCoupon.DISCOUNT_THRESHOLD_TRIGGER)
