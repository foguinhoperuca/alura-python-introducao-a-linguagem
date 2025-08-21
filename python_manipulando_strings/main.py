import logging
import sys

from url_manipulator import UrlParser
sys.path.append('.')
from util import Util  # noqa: E402


URL: str = 'https://python-string.alura.com.br/exchange?origin=BRL&destiny=USD&value=4.99'


def slice_string(vl: str, sep: str = '=') -> None:
    print(f'My first string: {vl}')
    index: int = vl.find(sep)
    print(f'arg is: {vl[:index]} value: {vl[index + 1:]}')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=Util.LOG_FORMAT_SIMPLE)

    vl: str = 'Some test for python string'
    print(f'My first string: {vl}')
    slice_string(vl='origin=BRL')

    print(f'Is valid URL? {UrlParser.validate_url(url=URL)}')

    url_parser: UrlParser = UrlParser(url=URL)

    url_parser.change_currency(currency_value='EUR', currency_type=UrlParser.PARAMS.DESTINY_CURRENCY)
    print('')
    print('actual url is:', url_parser.url)
    print('-------')
    print('')

    url_parser.change_currency(currency_value='GBP', currency_type=UrlParser.PARAMS.ORIGIN_CURRENCY)
    print('')
    print('actual url is:', url_parser.url)
    print('-------')
    print('')
