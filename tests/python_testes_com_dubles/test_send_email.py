from unittest.mock import patch

from tests.python_testes_com_dubles.util import send_email


def test_send_email():
    with patch("smtplib.SMTP") as mock_smtp:
        m = mock_smtp("localhost")
        send_email("from", "to", "body")
        m.sendmail.assert_called_once_with("from", "to", "body")
