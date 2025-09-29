from os import system
from time import sleep
from typing import Any, Dict, List

from first_course import first_course_menu
from second_course import second_course_menu
from third_course import third_course_menu
from models.restaurant import Client, Restaurant


if __name__ == "__main__":
    print('Start project: Sabor Express')

    while True:
        system('clear')
        print('Choose the course from formation:')
        print('1 - First Course')
        print('2 - Second Course')
        print('3 - Third Course')
        print('4 - Leave this program')
        course: int = int(input('Choose your destiny:\n--- '))

        restaurants: List[Restaurant] = [
            Restaurant.factory(name_factory='McDonalds', category_factory='Fast Food'),
            Restaurant.factory(name_factory='Fogo de Chão', category_factory='Brazilian Food'),
            Restaurant.factory(name_factory='Delícias de Paris', category_factory='French Food'),
            Restaurant.factory(name_factory='Mama Mia', category_factory='Italian Food'),
        ]
        client_portifolio: List[Client] = [
            Client.factory(client_id=1, name='Mary Adams', years=15),
            Client.factory(client_id=2, name='Jonh Keys', years=3),
            Client.factory(client_id=3, name='Mike Sculteler Senior', years=26),
            Client.factory(client_id=4, name='Mark Wilson Jr', years=7),
            Client.factory(client_id=5, name='Rose Ann Gutenberg', years=1)
        ]

        match course:
            case 1:
                should_leave: bool = first_course_menu()
                if should_leave:
                    break
            case 2:
                second_course_menu(clients=client_portifolio, restaurants=restaurants)
            case 3:
                third_course_menu(restaurants=restaurants)
            case 4:
                print('Leaving main menu... bye!!')
                sleep(1)
                break
            case _:
                print('Wrong choice. Choose the correct one: 1 - 3')

        sleep(1)
