from flask import render_template

from app.modules import Site
from .....abstracts.Subject import Subject
from .....abstracts.Observer import Observer

from .....services.EmailProvider.Email import EmailSender

from app.settings import app_variables

class MainFormEmailObserver(Observer):

    def update(self, subject: Subject) -> None:

        html_tempalte = render_template(
            'email.html',
            name=subject.username,
            email=subject.email,
            text=subject.message,
            url=subject.url,
            phone=subject.phone,
        )

        EmailSender.send_email(
            'Получена новая заявка с сайта',
            app_variables['SENDER_EMAIL'],
            ['newleads@1-sert.ru'],
            html_tempalte,
        )
