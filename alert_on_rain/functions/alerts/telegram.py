import telebot


class Telegram:

    def __init__(self, telegram_token):
        """
        Will create a telegram object

        Arguments:
            :param telegram_token: the telegram token
        """

        self.bot = telebot.TeleBot(telegram_token)

    def send_alert(self, chat_id):
        """
        Will send an alert about the rain via telegram

        Arguments:
            :param chat_id: the id of the telegram chat to send alerts to
        """

        message = """Subject: Rain tomorrow

            This message is to alert you it looks like it will rain tomorrow.
            """

        self.bot.send_message(chat_id, message)

