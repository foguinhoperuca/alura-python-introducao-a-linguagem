from time import sleep
from typing import Any, Dict, List

from web_requisition import get_remote_data
from models.restaurant import Restaurant
from models.menu import Bevarage, Desert, Dish, Item

default_menu: List[Item] = [
    Bevarage(name='Cueca Cuela', value=11.99, size=Bevarage.Size.SMALL),
    Bevarage(name='Soda', value=8.99, size=Bevarage.Size.MEDIUM),
    Dish(name='Parmeggiana', value=49.99, description='Individual dish'),
    Desert(name='Holand Pie', value=25.99, is_sweet=True)
]


def third_course_menu(restaurants: List[Restaurant]) -> None:
    print('Enter your option:')
    print('I - add an item to restaurant')
    print('L - list restaurants')
    print('R - Remote data')
    print('E - Exit this program')

    option = input('Choose your destiny!!\n --- ')
    print(f'You choosed {option}')

    match option.upper():
        case 'I':
            restaurant: Restaurant = Restaurant.filter_restaurant(restaurants=restaurants)
            for menu in default_menu:
                restaurant.menu = menu

            # WONTFIX make restaurants be a global index to be updated
            print('')
            print('| ---------- WARNING ---------- WARNING ---------- WARNING ---------- WARNING ---------- |')
            print('| This change in restaurant do not afect the restaurant in list restaurants: BE CAREFULL |')
            print('| ---------- WARNING ---------- WARNING ---------- WARNING ---------- WARNING ---------- |')
            print('')
            print(f'{restaurant=}')
            sleep(5)
        case 'L':
            restaurant: Restaurant = Restaurant.filter_restaurant(restaurants=restaurants)
            print(f'Menu in restaurant {restaurant}')
            for menu in restaurant.menu:
                print(f'{menu=}')

            sleep(5)
        case 'R':
            get_remote_data()
        case _:
            print(f'Option {option} not found!!')
            print('---')
            import this
