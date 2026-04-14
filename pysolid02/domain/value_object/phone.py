from typing import Self
import re


from pydantic import BaseModel, field_validator


class Phone(BaseModel):
    country_code: str
    area_code: str
    phone_number: str

    @field_validator('country_code')
    def _only_digits(cls, value: str) -> str:
        value = re.sub('[^0-9]', '', value)

        if not value:
            raise ValueError('[ONLY_DIGITS] Country Code invalid!!')

        return value

    @field_validator('country_code')
    def _validate_country_code(cls, value: str) -> str:
        if not (1 <= len(value) <= 3):
            raise ValueError('[VALIDATE_COUNTRY_CODE] Country Code invalid!!')

        return value

    @field_validator('area_code')
    def _validate_area_code(cls, value: str) -> str:
        if not (1 <= len(value) <= 3):
            raise ValueError('[VALIDATE_AREA_CODE] Area Code invalid!!')

        return value

    @field_validator('phone_number')
    def _validate_phone_number(cls, value: str) -> str:
        if not (8 <= len(value) <= 9):
            raise ValueError('[VALIDATE_PHONE_NUMBER] Phone Number invalid!!')

        return value

    def format_with_area_code(self: Self) -> str:
        return f'({self.area_code}) {self.phone_number}'

    def format_phone_number_complete(self: Self) -> str:
        return f'+[{self.country_code}] ({self.area_code}) - {self.phone_number}'

    def get_all_number(self: Self) -> str:
        return f'+{self.country_code}{self.area_code}{self.phone_number}'
