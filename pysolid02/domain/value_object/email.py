from typing import Self

from pydantic import BaseModel, EmailStr


class Email(BaseModel):
    address: EmailStr

    def domain(self: Self) -> str:
        return self.address.split['@'][1]
