import pytest
# from typing import Dict
# from unittest.mock import patch, Mock, mock_open
# from unittest import skip
# from urllib.error import HTTPError

from python_testes_com_dubles.books import consult_books


def test_consult_books_returns_format_string() -> None:
    result: str = consult_books('Agatha Christie')
    assert type(result) is str
