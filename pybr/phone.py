import logging
import re
from abc import ABC, abstractmethod
from util import Util


class GrahamBellPhone(ABC):
    def __init__(self, phone_number, pattern):
        self._pattern = pattern
        if self.validate(phone_number):
            self._phone_number = phone_number
        else:
            raise ValueError(f"Invalid phone number: {phone_number}")

    def __str__(self):
        return f"{self.mask()}"

    def __repr__(self):
        return f">> Type: {type(self)} -- phone number: {self.phone_number} <<"

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def pattern(self):
        return self._pattern

    def validate(self, phone_number):
        valid = False
        if re.findall(self._pattern, phone_number):
            valid = True

        logging.debug(f"Phone is valid? {Util.debug(valid)}")
        return valid

    @abstractmethod
    def mask(self):
        pass


class GenericPhone(GrahamBellPhone):
    PATTERN = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

    def __init__(self, phone_number):
        super(GenericPhone, self).__init__(phone_number=phone_number, pattern=GenericPhone.PATTERN)

    def mask(self):
        phone_snippets = re.search(GenericPhone.PATTERN, self.phone_number)
        logging.debug(phone_snippets)
        return f"+{'BRA' if phone_snippets.group(1) is None else phone_snippets.group(1)} ({phone_snippets.group(2)}) {phone_snippets.group(3)}-{phone_snippets.group(4)}"


class Landline(GrahamBellPhone):
    PATTERN = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"

    def __init__(self, phone_number):
        super(Landline, self).__init__(phone_number=phone_number, pattern=Landline.PATTERN)

    def mask(self):
        if len(self.phone_number) == 13:
            end_first_block = 9
        else:
            end_first_block = 10

        return f"+{self.phone_number[:3]} ({self.phone_number[3:5]}) {self.phone_number[5:end_first_block]}-{self.phone_number[end_first_block:]}"


class Mobile(GrahamBellPhone):
    PATTERN = "[0-9]{3}[0-9]{2}9[0-9]{4}[0-9]{4}"

    def __init__(self, phone_number):
        super(Mobile, self).__init__(phone_number=phone_number, pattern=Landline.PATTERN)

    def mask(self):
        return f"+{self.phone_number[:3]} ({self.phone_number[3:5]}) {self.phone_number[5:6]}.{self.phone_number[6:10]}-{self.phone_number[10:]}"
