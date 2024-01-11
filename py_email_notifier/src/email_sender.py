from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib
import ssl

class EmailSender:
    """
    Class for sending emails.
    """

    def __init__(
        self,
        sender_email: str,
        receiver_email: str,
        password: str
    ) -> None:

        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.password = password
        self.port = 465
        self.smtp_server = "smtp.gmail.com"


    def __get_html_message(
        self,
        script_name: str,
        function_name: str,
        message_text: list
    ):
        """
        Function to create the content of the email in html format.

        Args:
            script_name (str): Name of the script that has been executed.
            function_name (str): Name of the function that has been executed.
            message_text (list): Output of the function.
        """
        message = "\n".join(message_text)

        message = message.strip()

        html_header = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Bash Traceback Example</title>
                <style>
                    pre {
                        background-color: #f4f4f4;
                        padding: 10px;
                        text-indent: 0;
                        border: 1px solid #ddd;
                        font-family: 'Courier New', Courier, monospace;
                        max-width: 850px;
                    }
                </style>
            </head>
            <body>
        """

        script_part = "".join(("<p><b>Script name:</b> ", script_name, "</p>"))
        function_part = "".join(("<p><b>Function name:</b> ", function_name, "()", "</p>"))
        html_code_part = "".join(
            (
                "<p>Result of your program was: </p>", "<pre><code>",
                message,
                "</pre></code>"
            )
        )

        html_footer = """
            </body>
            </html>

        """

        # Create the formatedd html code
        html_code = "".join((
            html_header,
            script_part,
            function_part,
            html_code_part,
            html_footer
        ))

        return html_code


    def send_email(
        self,
        function_name: str,
        script_name: str,
        message_text: list
    ):
        """Function for sending the email.

        Args:
            script_name (str): Name of the script that has been executed.
            function_name (str): Name of the function that has been executed.
            message_text (list): Output of the function.
        """

        # Create the email
        message = MIMEMultipart("alternative")
        message["Subject"] = "".join(("Execution result of the function: ", function_name, "()"))
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        html_text = self.__get_html_message(
            function_name=function_name,
            script_name=script_name,
            message_text=message_text
        )
        text = MIMEText(html_text, "html")
        message.attach(text)

        # Send the email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(
                self.sender_email, self.receiver_email, message.as_string()
            )
