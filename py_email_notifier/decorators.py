"""
Python decorator to send the result of a long execution program
by email.

Usage Example:

    from py_email_notifier import send_result_email

    def test():
        a = [1,2]
        print(a[3])


    @send_result_email(
        sender_email="sender@email.com",
        receiver_email="receiver@email.com",
        password="sender-email-password"
    )
    def main():
        print("Python script for testing PyEmailNotifier")
        test()


Created by Iñigo Gabirondo López.
"""

import traceback
import os

from py_email_notifier.src.stdout_capturer import StdoutCapturer
from py_email_notifier.src.email_sender import EmailSender

def send_result_email(
    sender_email: str,
    receiver_email: str,
    password: str
):
    """Python decorator for sending the result of the function
    by email.

    Args:
        sender_email (str): Email that sends the result.
        receiver_email (str): Email that receives the result.
        password (str): Password of the sending email.
    """

    def decorator(func):
        def wrapper():
            with StdoutCapturer() as output:
                try:
                    func()

                except Exception:
                    print(traceback.format_exc())

            email_sender = EmailSender(
                sender_email=sender_email,
                receiver_email=receiver_email,
                password=password
            )

            filename = os.path.basename(__file__)
            function_name = func.__name__

            email_sender.send_email(
                function_name=function_name,
                script_name=filename,
                message_text=output
            )

        return wrapper

    return decorator
