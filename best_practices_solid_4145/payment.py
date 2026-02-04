from abc import ABC, abstractmethod
from decimal import Decimal
from enum import auto, Enum
import logging
from typing import Self


class PaymentStatus(Enum):
    PROCESSING = auto()
    SUCCESS = auto()
    ERROR = auto()


class PaymentType(Enum):
    CREDIT_CARD = auto()
    PIX = auto()
    UNSUPPORTED = auto()


class Payment(ABC):
    @abstractmethod
    def process(self: Self, value: Decimal) -> PaymentStatus:
        ...


class CreditCard(Payment):
    def process(self: Self, value: Decimal) -> PaymentStatus:
        logging.info(f'Processing payment by CREDIT CARD ${round(value, 2)}')

        status: PaymentStatus = PaymentStatus.PROCESSING

        if value > Decimal('5.00'):
            status = PaymentStatus.SUCCESS
        else:
            status = PaymentStatus.ERROR
            logging.warning('Value too low!!')

        print(f'Processed ${round(value, 2)} with status {status.name}')

        return status


class Pix(Payment):
    def process(self: Self, value: Decimal) -> PaymentStatus:
        logging.info(f'Processing payment by PIX ${round(value, 2)}')

        status: PaymentStatus = PaymentStatus.SUCCESS
        print(f'Processed ${round(value, 2)} with status {status.name}')

        return status


class PaymentFactory:
    @staticmethod
    def manufacture(payment_type: PaymentType) -> Payment:
        if payment_type is PaymentType.CREDIT_CARD:
            return CreditCard()
        elif payment_type is PaymentType.PIX:
            return Pix()

        logging.error(f'{payment_type} not supported')
        raise ValueError(f'{payment_type.name if isinstance(payment_type, PaymentType) else payment_type} not supported')
