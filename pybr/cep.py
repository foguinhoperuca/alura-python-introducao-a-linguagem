import logging
import re
import requests
from util import Util


class SearchAddress:
    PATTERN = "([0-9]{5})([0-9]{3})"

    def __init__(self, cep):
        if self.validate(cep):
            self._cep = cep
        else:
            raise ValueError(f"Invalid phone number: {cep}")

    def __str__(self):
        return self.mask()

    @property
    def cep(self):
        return self._cep

    def validate(self, cep):
        regex_validation = re.findall(SearchAddress.PATTERN, cep)
        if not (len(cep) == 8 and regex_validation):
            raise ValueError(f"Failed validate CEP with {len(cep) = } and {regex_validation = }")

        valid = True
        logging.debug(f"CEP is valid? {Util.debug(valid)}")

        return valid

    def mask(self):
        snippets = re.search(SearchAddress.PATTERN, self.cep)

        return f"{snippets.group(1)}-{snippets.group(2)}"

    def webservice(self):

        # cep
        # logradouro
        # complemento
        # bairro
        # localidade
        # uf
        # ibge
        # gia
        # ddd
        # siafi
        response = requests.get(f"http://viacep.com.br/ws/{self._cep}/json/")
        # print(type(response))
        # print(dir(response))
        # print(type(response.text))
        # print(type(response.json()))
        return response.json()
