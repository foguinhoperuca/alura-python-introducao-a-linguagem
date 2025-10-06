from typing import Dict
from unittest.mock import patch
from unittest import skip

from python_testes_com_dubles.books import consult_books


@skip('Not implemented yet!')
def test_consult_books_returns_format_string() -> None:
    assert type(consult_books('Agatha Christie')) == str


def test_consult_books_call_prepare_data_once_and_with_same_parameters() -> None:
    with patch('python_testes_com_dubles.books.prepare_data') as double_stunt:
        consult_books('Agatha Christie')
        double_stunt.assert_called_once_with(author='Agatha Christie')


def test_consult_books_call_get_url_with_params_return_of_prepare_data() -> None:
    author: str = 'Agatha Christie'
    url: str = 'https://search-online.com'
    with patch('python_testes_com_dubles.books.prepare_data') as double_stunt_prepare:
        data: Dict[str, str] = {
            'author': author
        }
        double_stunt_prepare.return_value = data

        with patch('python_testes_com_dubles.books.get_url') as double_stunt_get:
            consult_books(author)
            double_stunt_get.assert_called_once_with(url=url, data=data)

    with patch('python_testes_com_dubles.books.prepare_data') as double_stunt_prepare2:
        data2: Dict[str, str] = {}
        double_stunt_prepare2.return_value = data2

        with patch('python_testes_com_dubles.books.get_url') as double_stunt_get2:
            consult_books(author)
            double_stunt_get2.assert_called_once_with(url=url, data=data2)


def test_consult_books_call_execute_requisition_with_get_url_returns() -> None:
    author: str = 'Agatha Christie'
    url: str = 'https://search-online.com'
    with patch('python_testes_com_dubles.books.get_url') as double_stunt_get:
        double_stunt_get.return_value = url
        with patch('python_testes_com_dubles.books.execute_requisition') as double_stunt_execute:
            consult_books(author)
            double_stunt_execute.assert_called_once_with(url=url)
