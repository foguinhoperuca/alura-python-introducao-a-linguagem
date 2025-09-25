from os import system
from time import sleep
from typing import Any, Dict, List

from first_course import first_course_menu
from second_course import second_course_menu


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

        match course:
            case 1:
                should_leave: bool = first_course_menu()
                if should_leave:
                    break
            case 2:
                second_course_menu()
            case 3:
                pass
            case 4:
                print('Leaving main menu... bye!!')
                sleep(1)
                break
            case _:
                print('Wrong choice. Choose the correct one: 1 - 3')

        sleep(1)
