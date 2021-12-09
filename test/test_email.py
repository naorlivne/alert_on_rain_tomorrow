from unittest import TestCase, mock
from alert_on_rain.functions.alerts.email import *


class BaseTests(TestCase):

    @mock.patch("smtplib.SMTP_SSL")
    def test_email(self, mock_smtp):
        email_alert("localhost", "sender_email@test.com", "receiver_email@test.com", "password", "rain", 1025)
        message = 'Subject: Rain tomorrow' \
                  '\n\n    This message is to alert you it looks like it will be rainy tomorrow.\n    '
        mock_smtp.return_value.sendmail.assert_called_once_with("sender_email@test.com", "receiver_email@test.com",
                                                                message)
