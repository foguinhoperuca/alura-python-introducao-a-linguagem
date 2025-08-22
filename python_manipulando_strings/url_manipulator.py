from enum import StrEnum
import logging
import re
from typing import Self


class UrlParser:
    DEFAULT_ORIGIN_CURRENCY: str = 'BRL'
    DEFAULT_DESTINY_CURRENCY: str = 'USD'

    class SEP(StrEnum):
        VALUE = '='
        PARAM = '&'

    class PARAMS(StrEnum):
        ORIGIN_CURRENCY = 'origin'
        DESTINY_CURRENCY = 'destiny'
        VALUE = 'value'

    def __init__(self: Self, url: str) -> None:
        if not UrlParser.validate_url(url):
            raise ValueError(f'Invalid url: {url}')

        self.__url: str = url

    def __len__(self: Self) -> int:
        return len(self.__url)

    def __str__(self: Self) -> str:
        return self.__url

    def __repr__(self: Self) -> str:
        return self.__str__()

    def __eq__(self: Self, other: Self) -> bool:
        logging.debug("local: {} other: {}".format(self, other))

        return self.url == other.url

    @property
    def url(self: Self) -> str:
        return self.__url

    @staticmethod
    def validate_url(url: str) -> bool:
        return url and url.startswith('https://')

    def _get_param_index(self, param: PARAMS) -> int:
        full_param: str = f'{param}='
        logging.debug(f'full_param: {full_param}')

        return self.__url.find(full_param) + len(full_param)

    def change_currency(self, currency_value: str = DEFAULT_ORIGIN_CURRENCY, currency_type: PARAMS = PARAMS.ORIGIN_CURRENCY) -> None:
        param_index: int = self._get_param_index(param=currency_type)
        currency_current_value_end_index: int = self.__url[param_index:].find('&')
        currency_current_value: str = self.__url[param_index:(param_index + currency_current_value_end_index)]
        self.__url = self.__url.replace(f'{currency_type}={currency_current_value}', f'{currency_type}={currency_value.upper()}')

        logging.debug(f'param index: {param_index}')
        logging.debug(f'currency current_value end index: {currency_current_value_end_index}')
        logging.debug(f'currency_current_value {currency_current_value}')
        logging.debug(f'changed url with {currency_value} in {currency_type} and url now: {self.__url}')

    def get_value(self: Self) -> float:
        vl: float = None
        value_index: int = self.__url.find(f'{UrlParser.PARAMS.VALUE}=')
        raw_value: str = self.__url[(value_index + len(f'{UrlParser.PARAMS.VALUE}=')):]
        raw_value = raw_value.replace(',', '.')
        if re.search('[0-9]*\.[0-9]{2}', raw_value):
            vl = float(raw_value)

        logging.debug(f'{value_index}')
        logging.debug(f'{raw_value}')
        logging.debug(f'{vl}')

        return vl
