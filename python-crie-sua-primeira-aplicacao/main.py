from enum import StrEnum
from os import system
from time import sleep
from typing import Any, Dict, List


class Categories(StrEnum):
    FAST_FOOD = 'Fast Food'
    ITALIAN = 'Italian Food'
    BRAZILIAN = 'Brazilian Food'
    FRENCH = 'French Food'
    JAPANESE = 'Japanese Food'
    CHINESE = 'Chinese Food'


restaurants: List[Dict[str, Any]] = []


def create_restaurant() -> None:
    print('Create a restaurant...')
    name: str = input('Inform the name of restaurant:\n')
    while True:
        cat: str = input('Inform the category:\n')
        match cat:
            case '1':
                category: Categories = Categories.FAST_FOOD
                break
            case '2':
                category: Categories = Categories.ITALIAN
                break
            case '3':
                category: Categories = Categories.BRAZILIAN
                break
            case '4':
                category: Categories = Categories.FRENCH
                break
            case '5':
                category: Categories = Categories.JAPANESE
                break
            case '6':
                category: Categories = Categories.CHINESE
                break
            case _:
                print('Should you choose 1 - 6')
                sleep(1)

    active: bool = bool(int(input('Is active? 1 or any - YES or 0 - NO\n')))

    restaurants.append({'name': name, 'category': category, 'active': active})


def list_restaurant() -> None:
    print('List a restaurant...')
    for restaurant in restaurants:
        print(f'Name......: {restaurant["name"]}')
        print(f'Category..: {restaurant["category"].value}')
        if restaurant["active"]:
            print('Restaurant is ACTIVE')
        else:
            print('Restaurant is INACTIVE')

        print('--------------------')


def active_restaurant() -> None:
    print('--- Active a restaurant ---')

    while True:
        name: str = input("Inform the restaurant's name\n")
        restaurant: List[Dict[str, Any]] = list(filter(lambda r: r['name'] == name, restaurants))
        if len(restaurant) == 0:
            print(f'Restaurant {restaurant} not found!!')
            continue

        print(f'Restaurant founded: {restaurant}')
        restaurant[0]['active'] = not restaurant[0]['active']
        print(f'Restaurant after: {restaurant}')
        sleep(5)
        break


if __name__ == "__main__":
    print('Start project: Sabor Express')
    option: str = ''
    not_found_first_time: bool = True

    while True:
        system('clear')
        print('Enter your options:')
        print('1 - Create a restaturant')
        print('2 - List restaturants')
        print('3 - Activate a restaturant')
        print('4 - Leave this program')

        try:
            option = int(input('Choose your destiny!!\n'))
            print('---')
            print(f'You choosed {option}')

            match option:
                case 1:
                    create_restaurant()
                case 2:
                    list_restaurant()
                case 3:
                    active_restaurant()
                case 4:
                    print('Leaving...')
                    break
                case _:
                    print(f'Option {option} not found!!')
                    print('---')
                    if not_found_first_time:
                        import this
                        print('---')
                        not_found_first_time = False

            option = None
            sleep(2)
        except Exception as e:
            option = ''
            print(f"You've choosed a wrong option. Use number from 1 to 4. - error: {e}")
            sleep(1)
