from flask import Blueprint

# Register observers
from .features.MainForm.MainFormSubject import MainFormSubject as Subject
from .features.MainForm.MainFormEmailObserver import MainFormEmailObserver as EmailObserver
from .features.MainForm.MainFormSlackObserver import MainFormSlackObserver as SlackObserver

# Initialize subject class
main_form_subject = Subject()
# Initiate observers
email_observer = EmailObserver()
slack_observer = SlackObserver()
# Subscribe for updates
main_form_subject.attach(email_observer)
main_form_subject.attach(slack_observer)

site = Blueprint('site', __name__, template_folder='templates')
from .controllers import main_form_controller