from time import sleep
from typing import Any, Dict, List

from models.music import Music, music_factory
from models.restaurant import Client, Restaurant, Review


musics: List[Music] = []
restaurants: List[Restaurant] = [
    Restaurant.factory(name_factory='McDonalds', category_factory='Fast Food'),
    Restaurant.factory(name_factory='Fogo de Chão', category_factory='Brazilian Food'),
    Restaurant.factory(name_factory='Delícias de Paris', category_factory='French Food'),
    Restaurant.factory(name_factory='Delícias de Paris', category_factory='French Food'),
]
client_portifolio: List[Client] = [
    Client.factory(client_id=1, name='Mary Adams', years=15),
    Client.factory(client_id=2, name='Jonh Keys', years=3),
    Client.factory(client_id=3, name='Mike Sculteler Senior', years=26),
    Client.factory(client_id=4, name='Mark Wilson Jr', years=7),
    Client.factory(client_id=5, name='Rose Ann Gutenberg', years=1)
]


def second_course_menu() -> None:
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
                print(f'{"Name".ljust(30)} | {"Category".ljust(20)} | {"Is Active?".ljust(15)} | {"Rating".ljust(10)} |')
                for restaurant in restaurants:
                    print(f'{restaurant.name.ljust(30)} | {restaurant.category.value.ljust(20)} | {restaurant.is_active().ljust(15)} | {str(restaurant.avarage_rating()).ljust(10)} |')
            case 'R':
                while True:
                    name: str = input("Inform the restaurant's name:\n")
                    rests: List[Dict[str, Any]] = list(filter(lambda r: r.name == name, restaurants))
                    if len(rests) == 0:
                        print(f'Restaurant {name} not found!!')
                        continue

                    restaurant: Restaurant = rests[0]
                    restaurant.reviews = Review(client=client_portifolio[0], rating=3)
                    restaurant.reviews = Review(client=client_portifolio[1], rating=2)
                    restaurant.reviews = Review(client=client_portifolio[2], rating=5)

                    print(f'Restaurant {restaurant.name} has rating of {restaurant.avarage_rating()}')
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
