from unittest import TestCase, mock
from alert_on_rain.functions.alerts.telegram import *


class BaseTests(TestCase):

    @mock.patch("smtplib.SMTP_SSL")
    def test_telegram_init(self):
        pass

    def test_telegram_send_alert(self):
        pass
