from client import Client
from item import Item


client: Client = Client('Jonh', 'Alura')
pizza: Item = Item('Pizza', 30.0)
soda: Item = Item('Soda', 5.0)

print(f'Item: {pizza.name} price: {pizza.price}')
