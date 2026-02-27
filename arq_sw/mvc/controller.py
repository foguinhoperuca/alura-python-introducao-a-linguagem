import logging
from typing import List

from model import Attendant
from util import DEFAULT_LOGGER_NAME


attendants: List[Attendant] = []
view = None
logger = logging.getLogger(DEFAULT_LOGGER_NAME)


def set_view(_view) -> None:
    global view
    view = _view


def add(name: str, sales: int = 0) -> None:
    if name in [a.name for a in attendants]:
        view.alert(title='Name Validation', msg='Name duplicated. Enter ANOTHER name.')
        return

    attendants.append(Attendant(name=name, sales=sales))

    view.update()


def reset() -> None:
    attendants.clear()
    view.update()


def sales(name: str, sales: int = 1) -> None:
    attendant: Attendant = list(filter(lambda a: a.name == name, attendants))[0]
    logger.debug(f'{name=} ::: {sales=} ::: {str(attendant)}')

    attendant.increase_sales(sales=sales)
    view.update()


def order() -> None:
    attendants.sort(key=lambda attendant: attendant.name)
    view.update()


def get_all() -> List[Attendant]:
    return attendants
