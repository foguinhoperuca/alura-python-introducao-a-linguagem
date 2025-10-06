from typing import Dict


DEFAULT_URL: str = 'https://search-online.com'


def consult_books(author: str = '') -> str:
    data: Dict[str, str] = prepare_data(author=author)
    url: str = get_url(url=DEFAULT_URL, data=data)
    result: str = execute_requisition(url=url)

    return result


def prepare_data(author: str = '') -> Dict[str, str]:
    data: Dict[str, str] = {
        'author': author
    }

    return data


def get_url(url: str, data: Dict[str, str]) -> str:
    return ''


def execute_requisition(url: str) -> str:
    pass
