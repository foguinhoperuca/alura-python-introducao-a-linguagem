from time import sleep
from typing import Any, Dict, List

from models.music import Music, music_factory
from models.restaurant import Restaurant, restaurant_factory


musics: List[Music] = []
restaurants: List[Restaurant] = []


def second_course_menu() -> None:
    """
    Menu options to first course.
    Returns True if need to leave
    """

    should_exit: bool = False

    print('Enter your option:')
    print('M - create a music')
    print('R - create a restaurant')
    print('S - See restaurant status')
    print('T - Toogle status')
    print('L - List Restaurant')
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
            case 'R':
                restaurant: Restaurant = restaurant_factory()
                restaurants.append(restaurant)
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
                print(f'{"Name".ljust(30)} | {"Category".ljust(20)} | {"Is Active?".ljust(15)}')
                for restaurant in restaurants:
                    print(f'{restaurant.name.ljust(30)} | {restaurant.category.value.ljust(20)} | {restaurant.is_active().ljust(15)}')
            case '?':
                pass
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
