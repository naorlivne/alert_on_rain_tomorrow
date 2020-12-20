from unittest import TestCase
from alert_on_rain.functions.alerts.telegram import *
import requests_mock


class BaseTests(TestCase):

    def test_telegram_init(self):
        telegram_object = Telegram("my_totally_real_telegram_token")
        self.assertEqual(telegram_object.bot.token, "my_totally_real_telegram_token")

    def test_telegram_send_alert(self):
        with requests_mock.Mocker() as request_mocker:
            request_mocker.post('https://api.telegram.org/botmy_totally_real_telegram_token/sendMessage?chat_id=123&'
                                'text=Subject%3A+Rain+tomorrow%0A%0A++++++++++++This+message+is+to+alert+you+it+looks'
                                '+like+it+will+rain+tomorrow.%0A++++++++++++',
                                status_code=200, text='{"ok":true,"result":{"message_id":85,"from":{"id":123,'
                                                      '"is_bot":true,"first_name":"blabla",'
                                                      '"username":"blablason"},"chat":{'
                                                      '"id":123,"first_name":"blabla","last_name":"son",'
                                                      '"username":"Naorlivne","type":"private"},"date":123,'
                                                      '"text":"test api is working"}}')
            telegram_object = Telegram("my_totally_real_telegram_token")
            reply = telegram_object.send_alert("123")
            self.assertTrue(reply.json['from']['is_bot'])
