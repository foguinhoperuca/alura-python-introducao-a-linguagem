from unittest.mock import patch

from python_testes_com_dubles.books import execute_requisition

from tests.python_testes_com_dubles.util import HTTPResponseStub


def stub_urlopen(url, timeout) -> HTTPResponseStub:
    return HTTPResponseStub()


def test_execute_requisition_returns_type_str_using_stub() -> None:
    url: str = 'https://search-online.com'
    with patch('python_testes_com_dubles.books.urlopen', stub_urlopen):
        result: str = execute_requisition(url=url)
        assert type(result) is str
