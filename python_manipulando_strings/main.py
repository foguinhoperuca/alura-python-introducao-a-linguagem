import logging
import sys

from url_manipulator import UrlParser
sys.path.append('.')
from util import Util  # noqa: E402


URL_00: str = 'https://python-string.alura.com.br/exchange?origin=BRL&destiny=USD&value=04,99'
URL_01: str = 'https://python-string.alura.com.br/exchange?origin=BRL&destiny=USD&value=04,99'
URL_02: str = 'https://python-string.alura.com.br/exchange?origin=BRL&destiny=USD&value=169.52'


def slice_string(vl: str, sep: str = '=') -> None:
    print(f'My first string: {vl}')
    index: int = vl.find(sep)
    print(f'arg is: {vl[:index]} value: {vl[index + 1:]}')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=Util.LOG_FORMAT_SIMPLE)

    vl: str = 'Some test for python string'
    print(f'My first string: {vl}')
    slice_string(vl='origin=BRL')

    print(f'Is valid URL? {UrlParser.validate_url(url=URL_00)}')

    url_parser_00: UrlParser = UrlParser(url=URL_00)
    url_parser_01: UrlParser = UrlParser(url=URL_01)
    url_parser_02: UrlParser = UrlParser(url=URL_02)
    print(f'equal? {URL_00 == URL_01} :: {url_parser_00 == url_parser_01}')
    print(f'equal? {URL_00 == URL_02} :: {url_parser_00 == url_parser_02}')

    url_parser_00.change_currency(currency_value='EUR', currency_type=UrlParser.PARAMS.DESTINY_CURRENCY)
    print('')
    print('actual url is:', url_parser_00.url)
    print('-------')
    print('')

    url_parser_00.change_currency(currency_value='GBP', currency_type=UrlParser.PARAMS.ORIGIN_CURRENCY)
    print('')
    print('actual url is:', url_parser_00.url)
    print('-------')
    print('')

    print(f'get value: {url_parser_00.get_value()}')
    assert url_parser_00.get_value() == 4.99
