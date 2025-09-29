from time import sleep
from typing import Any, Dict, List

from models.music import Music, music_factory
from models.restaurant import Client, Restaurant, Review


musics: List[Music] = []


def second_course_menu(clients: List[Client], restaurants: List[Restaurant]) -> None:
    """
    Menu options to first course.
    Returns True if need to leave
    """

    should_exit: bool = False

    print('Enter your option:')
    print('M - create a music')
    print('C - create a restaurant')
    print('S - See restaurant status')
    print('T - Toogle status')
    print('L - List Restaurant')
    print('R - Review a restaurant')
    print('? - ???')
    print('E - Exit this program')

    try:
        option = input('Choose your destiny!!\n --- ')
        print(f'You choosed {option}')

        match option.upper():
            case 'M':
                music: Music = music_factory()
                musics.append(music)
                print(f'List of Musics ({len(musics)} total)')
                for m in musics:
                    print(m)
            case 'C':
                restaurants.append(Restaurant.factory())
                print(f'List of Restaurants ({len(restaurants)} total)')
                for m in restaurants:
                    print(m)
            case 'S':
                for restaurant in restaurants:
                    print(f'{restaurant} is active: {restaurant.is_active()}:')
            case 'T':
                while True:
                    name: str = input("Inform the restaurant's name:\n")
                    rests: List[Dict[str, Any]] = list(filter(lambda r: r.name == name, restaurants))
                    if len(rests) == 0:
                        print(f'Restaurant {name} not found!!')
                        continue

                    restaurant: Restaurant = rests[0]
                    print(f'BEFORE..: {restaurant}')
                    restaurant.toggle_state()
                    print(f'AFTER...: {restaurant}')
                    break
            case 'L':
                print(f'{"Name".ljust(30)} | {"Category".ljust(20)} | {"Is Active?".ljust(15)} | {"Rating".ljust(10)} | {"Total Items Menu".ljust(20)}')
                for restaurant in restaurants:
                    print(f'{restaurant.name.ljust(30)} | {restaurant.category.value.ljust(20)} | {restaurant.is_active().ljust(15)} | {str(restaurant.avarage_rating).ljust(10)} | {str(len(restaurant.menu))}')
            case 'R':
                while True:
                    name: str = input("Inform the restaurant's name:\n")
                    rests: List[Dict[str, Any]] = list(filter(lambda r: r.name == name, restaurants))
                    if len(rests) == 0:
                        print(f'Restaurant {name} not found!!')
                        continue

                    restaurant: Restaurant = rests[0]
                    restaurant.reviews = Review(client=clients[0], rating=3)
                    restaurant.reviews = Review(client=clients[1], rating=2)
                    restaurant.reviews = Review(client=clients[2], rating=5)

                    print(f'Restaurant {restaurant.name} has rating of {restaurant.avarage_rating}')
                    break
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
