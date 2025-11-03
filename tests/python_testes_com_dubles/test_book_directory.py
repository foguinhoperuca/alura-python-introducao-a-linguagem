# import pytest
# from typing import Dict
from unittest.mock import MagicMock, patch
# from unittest import skip
# from urllib.error import HTTPError

from python_testes_com_dubles.books import write_in_file

from tests.python_testes_com_dubles.util import DoubleStuntLogging, SpyFp


def double_stunt_makedirs(directory: str) -> None:
    raise OSError(f"Couldn't create directory {directory}")


def test_write_file_register_error_on_create_directory() -> None:
    directory: str = '/tmp'
    filename: str = f'{directory}/filename.json'
    content: str = 'Book data'
    double_stunt_logging: DoubleStuntLogging = DoubleStuntLogging()
    with patch('python_testes_com_dubles.books.makedirs', double_stunt_makedirs):
        with patch('python_testes_com_dubles.books.logging', double_stunt_logging):
            write_in_file(filename, content)
            assert f"Couldn't create directory {directory}" in double_stunt_logging.messages


@patch('python_testes_com_dubles.books.makedirs')
@patch('python_testes_com_dubles.books.logging.exception')
@patch('python_testes_com_dubles.books.open', side_effect=OSError())
def test_write_file_register_error_on_create_file(stub_open, spy_exception, stub_makedirs) -> None:
    """
    Dev hint: the order os params in signature is inverse of order of @patch
    """
    filename: str = '/do_not_exist_directory/filename.json'
    content: str = 'Book data'
    write_in_file(filename, content)
    spy_exception.assert_called_once_with("Couldn't create filename /do_not_exist_directory/filename.json")


@patch('python_testes_com_dubles.books.open')
def test_write_in_file_call_write_spy_fp(stub_open) -> None:
    filename: str = '/tmp/filename'
    content: str = 'Book data'
    spy_fp: SpyFp = SpyFp()
    stub_open.return_value = spy_fp

    write_in_file(filename, content)
    assert spy_fp._content == content


@patch('python_testes_com_dubles.books.open')
def test_write_in_file_call_write(stub_open) -> None:
    filename: str = '/tmp/filename_call_write'
    content: str = 'Book data'
    """
    Dev hint: Using MagickMock also need define __enter__() and __exit__()
    """
    spy_fp: MagicMock = MagicMock()
    spy_fp.__enter__.return_value = spy_fp
    spy_fp.__exit__.return_value = None
    stub_open.return_value = spy_fp

    write_in_file(filename, content)
    spy_fp.write.assert_called_once_with(content)
