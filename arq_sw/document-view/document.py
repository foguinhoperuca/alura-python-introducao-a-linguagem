from typing import Dict, List


attendants: List[Dict[str, int]] = []


def add_attendants(name: str, sales: int = 0) -> str:
    if not name:
        return 'Name is empty. You must enter a name.'

    if name in [a['name'] for a in attendants]:
        return 'Name is duplicated. Enter ANOTHER name.'

    attendants.append({"name": name, "sales": sales})
    return 'OK'


def reset_attendants() -> None:
    attendants.clear()


def update_attendants(index: int) -> None:
    attendants[index]['sales'] += 1


def get_attendants() -> List[Dict[str, int]]:
    return attendants
