import logging
from typing import Dict
from urllib.request import urlopen
from urllib.error import HTTPError


DEFAULT_URL: str = 'https://search-online.com'


def consult_books(author: str = '') -> str:
    data: Dict[str, str] = prepare_data(author=author)
    url: str = get_url(url=DEFAULT_URL, data=data)
    result: str = execute_requisition(url=url)

    return result


def prepare_data(author: str) -> Dict[str, str]:
    data: Dict[str, str] = {
        'author': author
    }

    return data


def get_url(url: str, data: Dict[str, str]) -> str:
    pass


def execute_requisition(url: str, timeout: int = 10) -> str:
    try:
        with urlopen(url, timeout=timeout) as response:
            result: str = response.read().decode('utf-8')
    except HTTPError as e:
        # msg: str = f'Got some error in url {url} error: {e}'
        msg: str = 'error message'
        print(msg)
        logging.exception(msg)
    else:
        return result

    # with urlopen(url, timeout=timeout) as response:
    #     result: str = response.read().decode('utf-8')

    # return result
