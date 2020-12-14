import smtplib
import ssl


def email_alert(smtp_server: str, sender_email: str, receiver_email: str, password: str, port: int = 465):
    """
    Will send an email alert saying it looks like it will rain tomorrow

    Arguments:
        :param port: The SMTP server port, default to 465 for SSL
        :param smtp_server: The SMTP server URL
        :param sender_email: The sender email address
        :param receiver_email: The receiver email address
        :param password: The SMTP pass
    """
    password = str(password)
    message = """Subject: Rain tomorrow

    This message is to alert you it looks like it will rain tomorrow.
    """

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server, port, context=context)
    server.login(sender_email, password)
    email_result = server.sendmail(sender_email, receiver_email, message)
    return email_result
