import pytest
from typing import Dict
from unittest.mock import patch, Mock, mock_open
from unittest import skip
from urllib.error import HTTPError

from python_testes_com_dubles.books import consult_books, execute_requisition

from tests.python_testes_com_dubles.util import DEFAULT_ERROR_MESSAGE, DEFAULT_URL, Dummy, HTTPResponseStub


@patch('python_testes_com_dubles.books.urlopen', return_value=HTTPResponseStub())
def test_consult_books_returns_format_string(stub_urlopen) -> None:
    result: str = consult_books('Agatha Christie')

    assert type(result) is str


@patch('python_testes_com_dubles.books.urlopen', return_value=HTTPResponseStub())
def test_consult_books_call_prepare_data_once_and_with_same_parameters(stub_urlopen) -> None:
    with patch('python_testes_com_dubles.books.prepare_data') as spy_prepare_data:
        consult_books('Agatha Christie')
        spy_prepare_data.assert_called_once_with(author='Agatha Christie')


@patch('python_testes_com_dubles.books.urlopen', return_value=HTTPResponseStub())
def test_consult_books_call_get_url_with_params_return_of_prepare_data(stub_urlopen) -> None:
    author: str = 'Agatha Christie'
    url: str = DEFAULT_URL
    with patch('python_testes_com_dubles.books.prepare_data') as double_stunt_prepare:
        data: Dict[str, str] = {
            'author': author
        }
        double_stunt_prepare.return_value = data

        with patch('python_testes_com_dubles.books.get_url') as spy_get_url:
            consult_books(author)
            spy_get_url.assert_called_once_with(url=url, data=data)

    with patch('python_testes_com_dubles.books.prepare_data') as double_stunt_prepare2:
        data2: Dict[str, str] = {}
        double_stunt_prepare2.return_value = data2

        with patch('python_testes_com_dubles.books.get_url') as spy_get_url2:
            consult_books(author)
            spy_get_url2.assert_called_once_with(url=url, data=data2)


@patch('python_testes_com_dubles.books.urlopen', return_value=HTTPResponseStub())
def test_consult_books_call_execute_requisition_with_get_url_returns(stub_urlopen) -> None:
    author: str = 'Agatha Christie'
    url: str = 'https://buscador'
    with patch('python_testes_com_dubles.books.get_url') as double_stunt_get:
        double_stunt_get.return_value = url
        with patch('python_testes_com_dubles.books.execute_requisition') as spy_execute_requisition:
            consult_books(author)
            spy_execute_requisition.assert_called_once_with(url=url)


def test_execute_requisition_returns_type_str() -> None:
    url: str = 'https://search-online.com'
    with patch('python_testes_com_dubles.books.urlopen') as double_stunt_urlopen:
        double_stunt_urlopen.return_value = HTTPResponseStub()
        result: str = execute_requisition(url=url)
        assert type(result) is str


def test_execute_requisition_returns_type_str_form02() -> None:
    url: str = 'https://search-online.com'
    with patch('python_testes_com_dubles.books.urlopen', return_value=HTTPResponseStub()):
        result: str = execute_requisition(url=url)
        assert type(result) is str


@patch('python_testes_com_dubles.books.urlopen', return_value=HTTPResponseStub())
def test_execute_requisition_returns_type_str_form03(double_stunt_urlopen) -> None:
    url: str = 'https://search-online.com'
    result: str = execute_requisition(url=url)
    assert type(result) is str


@patch('python_testes_com_dubles.books.urlopen')
def test_execute_requisition_returns_type_str_form04(double_stunt_urlopen) -> None:
    double_stunt_urlopen.return_value = HTTPResponseStub()
    url: str = 'https://search-online.com'
    result: str = execute_requisition(url=url)
    assert type(result) is str


def stub_urlopen_raises_http_error(url, timeout) -> None:
    fp = mock_open
    fp.close = Dummy
    raise HTTPError(Dummy(), Dummy(), DEFAULT_ERROR_MESSAGE, Dummy(), fp)


@skip('Not working anymore')
def test_execute_requisition_raise_exception() -> None:
    url: str = 'https://search-online.com'
    with patch('python_testes_com_dubles.books.urlopen', stub_urlopen_raises_http_error):
        with pytest.raises(HTTPError) as exception:
            execute_requisition(url=url)

        assert DEFAULT_ERROR_MESSAGE in str(exception.value)


@skip('Not working anymore')
@patch('python_testes_com_dubles.books.urlopen')
def test_execute_requisition_raise_exception_mock(double_stunt_raise_exception) -> None:
    fp = mock_open
    fp.close = Mock()
    double_stunt_raise_exception.side_effect = HTTPError(Mock(), Mock(), DEFAULT_ERROR_MESSAGE, Mock(), fp)
    with pytest.raises(HTTPError) as exception:
        execute_requisition(url=DEFAULT_URL)
        assert DEFAULT_ERROR_MESSAGE in str(exception.value)


def test_execute_requisition_logging_http_error(caplog) -> None:
    with patch('python_testes_com_dubles.books.urlopen', stub_urlopen_raises_http_error):
        result = execute_requisition(url=DEFAULT_URL)
        print(result)
        assert len(caplog.records) == 1
        for record in caplog.records:
            assert DEFAULT_ERROR_MESSAGE in record.message


@patch('python_testes_com_dubles.books.urlopen')
def test_execute_requisition_raise_http_error_2_09(double_stunt_urlopen, caplog):
    fp = mock_open
    fp.close = Mock()
    double_stunt_urlopen.side_effect = HTTPError(Mock(), Mock(), DEFAULT_ERROR_MESSAGE, Mock(), fp)
    execute_requisition('http://')
    assert len(caplog.records) == 1

    for record in caplog.records:
        assert DEFAULT_ERROR_MESSAGE in record.message
