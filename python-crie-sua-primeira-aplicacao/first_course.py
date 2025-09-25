from time import sleep
from typing import Any, Dict, List

from models.restaurant import Categories


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

    restaurant: Dict[str, Any] = {'name': name, 'category': category, 'active': active}
    restaurants.append(restaurant)
    print(f'Added: {restaurant}')


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


def first_course_menu() -> bool:
    """
    Menu options to first course.
    Returns True if need to leave
    """

    should_exit: bool = False

    print('Enter your option:')
    print('C - Create a restaturant')
    print('L - List restaturants')
    print('A - Activate a restaturant')
    print('E - Exit this program')

    try:
        option = input('Choose your destiny!!\n --- ')
        print(f'You choosed {option}')

        match option.upper():
            case 'C':
                create_restaurant()
            case 'L':
                list_restaurant()
            case 'A':
                active_restaurant()
            case 'E':
                print('Leaving...')
                should_exit = True
            case _:
                print(f'Option {option} not found!!')
                print('---')
                import this
    except Exception as e:
        option = ''
        print(f"You've choosed a wrong option. {option=}. - error: {e}")
        should_exit = True

    sleep(2)
    return should_exit
