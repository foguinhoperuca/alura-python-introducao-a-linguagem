from decimal import Decimal
import logging
from typing import List

from client import Client
from item import Item
from order import Delivery, Gift, Order, Special, Takeout
from payment import Payment, PaymentFactory, PaymentStatus, PaymentType
from notification import NotificationFacade
from util import LOG_FORMAT_INFO


logging.basicConfig(level=logging.INFO, format=LOG_FORMAT_INFO)
if __name__ == "__main__":
    credit_card: Payment = PaymentFactory.manufacture(PaymentType.CREDIT_CARD)
    pix: Payment = PaymentFactory.manufacture(PaymentType.PIX)
    notification: NotificationFacade = NotificationFacade()

    client: Client = Client('John', 'rua da Alura')
    pizza: Item = Item('Pizza', 30.0)
    soda: Item = Item('Soda', 5.0)
    itens: List[Item] = [pizza, soda]
    delivery: Order = Delivery(client=client, itens=itens, delivery_fee=Decimal(3.00))
    print(f'{delivery}')
    john_payment: PaymentStatus = credit_card.process(value=delivery.total())
    if john_payment is PaymentStatus.SUCCESS:
        notification.send(client=client, message=f'Your order with {len(itens)} is ready to go!')
    print('----------')

    albert: Client = Client('Albert', 'Back St., 231')
    burguer: Item = Item(name='Burguer', price=45.00)
    beer: Item = Item(name='Beer', price=15.00)
    albert_cart: List[Item] = [burguer, beer]
    takeout: Order = Takeout(client=albert, itens=albert_cart)
    print(f'{takeout}')
    albert_payment: PaymentStatus = pix.process(value=takeout.total())
    if albert_payment is PaymentStatus.SUCCESS:
        notification.send(client=albert, message=f'Your order with {len(albert_cart)} is ready to go!')
    print('----------')

    mark: Client = Client('Mark E', 'Front St., 85')
    french_fries: Item = Item(name='French Fries', price=9.00)
    orange_juice: Item = Item(name='Orange Juice', price=19.00)
    mark_cart: List[Item] = [french_fries, orange_juice]
    gift: Order = Gift(client=mark, itens=mark_cart, gift_card=Gift.GiftCardType.URGENT)
    print(f'{gift}')
    mark_payment: PaymentStatus = pix.process(value=gift.total())
    if mark_payment is PaymentStatus.SUCCESS:
        notification.send(client=mark, message=f'Your order with {len(mark_cart)} is ready to go!')
    print('----------')

    joseph: Client = Client('Joseph', 'Down St., 416')
    xburguer: Item = Item(name='X-Burguer', price=48.00)
    light_soda: Item = Item('Light Soda', 8.00)
    joseph_cart: List[Item] = [xburguer, light_soda]
    special: Order = Special(client=joseph, itens=joseph_cart)
    print(f'{special}')
    joseph_payment: PaymentStatus = credit_card.process(value=special.total())
    if joseph_payment is PaymentStatus.SUCCESS:
        notification.send(client=joseph, message=f'Your order with {len(joseph_cart)} is ready to go!')

    try:
        another_invalid_payment: Payment = PaymentFactory.manufacture(PaymentType.UNSUPPORTED)
    except Exception as e:
        logging.warning(f'Error with payments -> {e}')
