import smtplib
from typing import Any, List, Optional, Self

DEFAULT_ERROR_MESSAGE: str = 'error message'
DEFAULT_URL: str = 'https://search-online.com'


class HTTPResponseStub:
    def read(self) -> bin:
        return b''

    def __enter__(self) -> Self:
        return self

    def __exit__(self, param1, param2, param3):
        pass


class Dummy:
    """
    It 's a empty/void souble stunt class used to replace mandatory parameters. It isn't relevat to tests.
    """
    pass


class DoubleStuntLogging:
    """
    Mock python standard module logging to use an spy in test.
    """
    def __init__(self: Self) -> None:
        self._messages: List[Any] = []

    @property
    def messages(self: Self) -> List[Any]:
        return self._messages

    def exception(self: Self, message: Any) -> None:
        self._messages.append(message)


class SpyFp:
    def __init__(self: Self) -> None:
        self._content: Optional[Any] = None

    def __enter__(self: Self) -> Self:
        return self

    def __exit__(self: Self, param1: Any, param2: Any, param3: Any) -> None:
        pass

    def write(self: Self, content: Any) -> None:
        self._content = content


def send_email(fromaddr, toaddrs, msg):
    server = smtplib.SMTP('localhost')
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
