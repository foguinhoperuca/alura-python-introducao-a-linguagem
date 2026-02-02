from decimal import Decimal
import logging
from typing import List

from client import Client
from item import Item
from order.order import Delivery, Order, Takeout
from util import LOG_FORMAT_INFO


logging.basicConfig(level=logging.INFO, format=LOG_FORMAT_INFO)
if __name__ == "__main__":
    client: Client = Client('John', 'rua da Alura')
    pizza: Item = Item('Pizza', 30.0)
    soda: Item = Item('Soda', 5.0)
    itens: List[Item] = [pizza, soda]
    delivery: Order = Delivery(client=client, itens=itens, delivery_fee=Decimal(3.00))
    print(f'{delivery}')

    albert: Client = Client('Albert', 'Back St., 21')
    burguer: Item = Item(name='Burguer', price=45.00)
    beer: Item = Item(name='Beer', price=15.00)
    itens: List[Item] = [burguer, beer]
    takeout: Order = Takeout(client=albert, itens=[burguer, beer])
    print(f'{takeout}')
