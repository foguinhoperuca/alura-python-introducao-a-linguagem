import logging
import re
from decimal import Decimal
from util import Util


class ExtractorCEP:
    @staticmethod
    def parse(address="18090-380"):
        logging.warning(address)

        pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
        search = pattern.search(address)
        if search:
            res = search.group()
            print(f"{res=}")


class ExtractorUrl:
    DOLAR = Decimal(5.00)

    def __init__(self, url="http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"):
        self.__url = ExtractorUrl.validate_url(ExtractorUrl.sanitize(url))

    def __len__(self):
        return len(self.__url)

    def __str__(self):
        return f"Base: {ExtractorUrl.get_url_base(self.__url)} -- Params: {ExtractorUrl.get_url_params(self.__url)}"

    def __eq__(self, other):
        return self.__url == other.url

    @property
    def url(self):
        return self.__url

    @staticmethod
    def get_url_base(url):
        base = ""
        if url.find('?') != -1:
            base = url[:url.find('?')]
        else:
            base = url[:len(url)]

        return base

    @staticmethod
    def get_url_params(url):
        return url[(url.find("?") + 1):]

    @staticmethod
    def sanitize(original_url: str) -> str:
        logging.debug(original_url)
        if type(original_url) == str:
            tmp = original_url.strip()
            tmp = tmp.replace(" ", "")
        else:
            tmp = ""

        return tmp

    @staticmethod
    def validate_url(sanitized_url: str) -> str:
        logging.debug(f"{sanitized_url=} {(not sanitized_url)=}")
        if not sanitized_url:
            raise ValueError("No empty URL is allowed!")

        # if not sanitized_url.startswith("http://"):
        #     raise ValueError("No protocol informed!")
        #
        # if not ExtractorUrl.get_url_base(sanitized_url).endswith("/cambio"):
        #     raise ValueError("No route informed!")

        pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        matched = pattern.match(sanitized_url)

        if not matched:
            raise ValueError("URL is not valid. Regex failed!!")

        return sanitized_url

    def get_param_value(self, search_param):
        params = self.__url[(self.__url.find("?") + 1):]
        value = ""

        param_position = params.find(search_param)
        ampersand_position = params.find('&', param_position)
        logging.debug(Util.debug(f"{params=} {search_param=} {params.find(search_param)=} {ampersand_position=}"))

        if ampersand_position == -1:
            value = params[param_position + (len(search_param) + 1):]
        else:
            value = params[param_position + (len(search_param) + 1):ampersand_position]

        logging.debug(Util.debug(f"value is: {value} {len(value)=}"))

        return value

    def convert(self, currency):
        value = self.get_param_value("quantidade")
        converted = 0.00
        if currency == "real":
            converted = Decimal(value) * ExtractorUrl.DOLAR
        else:
            converted = Decimal(value) / ExtractorUrl.DOLAR

        return converted
