from flask_mail import Message
import app
from typing import List

class EmailSender:

    def send_email(subject: str, sender: str, recipients: List[str], html_template: str):

        msg = Message(
            subject=subject,
            sender=sender,
            recipients=recipients,
            html=html_template
        )

        try:
            app.mail.send(msg)
        except:
            raise BaseException()
