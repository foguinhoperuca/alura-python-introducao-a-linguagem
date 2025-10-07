from typing import Self


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
