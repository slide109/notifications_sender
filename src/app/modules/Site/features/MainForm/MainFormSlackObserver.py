from flask import render_template
from app.modules import Site
from .....abstracts.Subject import Subject
from .....abstracts.Observer import Observer
from .....services.SlackProvider.Slack import SlackNotificationSender
from ...templates import slack_message

from app.settings import app_variables

class MainFormSlackObserver(Observer):
    def update(self, subject: Subject) -> None:

        message = slack_message.create_slack_message(
            subject.username,
            subject.email,
            subject.url,
            subject.phone,
            subject.message,
            subject.productName,
            subject.price,
        )

        SlackNotificationSender.send_message(app_variables['SLACK_CHANNEL_ID'], message)