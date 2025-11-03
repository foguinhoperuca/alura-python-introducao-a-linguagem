from json import JSONDecodeError, loads
import logging
from math import ceil
from os import makedirs
from os.path import dirname
from typing import Any, Dict, List, Optional, Self
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen, Request


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
        msg: str = 'error message'
        print(msg, f' :: for url {url} message is {e}')
        logging.exception(msg)
    else:
        return result

    # with urlopen(url, timeout=timeout) as response:
    #     result: str = response.read().decode('utf-8')

    # return result


def write_in_file(filename: str, content: str) -> None:
    directory: str = dirname(filename)
    msg: str = ''
    try:
        makedirs(directory)
    except OSError as e:
        msg = f"Couldn't create directory {directory}"
        print(msg, f' :: {e}')
        logging.exception(msg)

    try:
        with open(filename, 'w') as fp:
            fp.write(content)
    except OSError as e:
        msg = f"Couldn't create filename {filename}"
        print(msg, f' :: {e}')
        logging.exception(msg)


class BookConsult:
    def __init__(self: Self, author: Optional[str] = None, title: Optional[str] = None, free_query: Optional[str] = None) -> None:
        self._author: str = author
        self._title: str = title
        self._free_query: str = free_query
        self._page: int = 0
        self._requisition_data: Optional[Dict[str, Any]] = None
        self._url: str = DEFAULT_URL

    @property
    def page(self: Self) -> int:
        return self._page

    @property
    def requisition_data(self: Self) -> Optional[Dict[str, Any]]:
        if not self._requisition_data:
            self._requisition_data = {}
            if self._free_query:
                self._requisition_data = {'q': self._free_query}
            else:
                if self._author:
                    self._requisition_data['author'] = self._author

                if self._title:
                    self._requisition_data['title'] = self._title

        return self._requisition_data

    @property
    def next(self: Self) -> Optional[str]:
        requisition_data: Optional[Dict[str, Any]] = self.requisition_data
        self._page += 1
        requisition_data['page'] = self._page
        req: Optional[Request] = Request(self._url, requisition_data)
        if req.data:
            return f'{req.full_url}?{urlencode(req.data)}'


class BookResponse:
    TOTAL_DOCS_PER_PAGE: int = 50

    def __init__(self: Self, content: Any) -> None:
        self._content: Any = content
        self._data: Optional[Any] = None

    @property
    def content(self: Self) -> Any:
        return self._content

    @property
    def data(self: Self) -> Any:
        if not self._data:
            try:
                j = loads(self._content)
            except TypeError as e:
                logging.exception(f'Result of free_query consult is {self._content}: invalid TYPE - error {e}')
            except JSONDecodeError as e:
                logging.exception(f'Result of free_query consult is {self._content}: invalid JSONDECODEERROR - error {e}')
            else:
                self._data = j

        return self._data

    @property
    def documents(self: Self) -> Any:
        return self._data.get('docs', [])

    @property
    def total_pages(self: Self) -> int:
        if len(self.documents):
            return ceil(self._data.get('num_docs', 0) / self.TOTAL_DOCS_PER_PAGE)

        return 0


def download_books(filename: List[str], author: Optional[str] = None, title: Optional[str] = None, free_query: Optional[str] = None) -> None:
    i: int = 0
    total_pages: int = 1
    book_consult: BookConsult = BookConsult(author=author, title=title, free_query=free_query)

    while True:
        result: str = execute_requisition(url=book_consult.next)
        if result:
            response: BookResponse = BookResponse(content=result)
            total_pages = response.total_pages
            write_in_file(filename[i], result)
        elif consult_books.page == 1:
            total_pages = 2

        if consult_books.page == total_pages:
            break

        i += 1


def read_file(name: str) -> str:
    return ''


def book_recording(filenames: List[str], insert_record) -> int:
    quantity: int = 0
    for filename in filenames:
        content: str = read_file(name=filename)
        response: BookResponse = BookResponse(content=content)
        quantity += insert_record(response.documents)

    return quantity
