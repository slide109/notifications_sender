import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

app_variables = {
    'MAIL_SERVER':      os.getenv('MAIL_SERVER'),
    'MAIL_PORT':        587,
    'MAIL_USE_TLS':     True,
    'MAIL_USE_SSL':     False,
    'MAIL_USERNAME':    os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD':    os.getenv('MAIL_PASSWORD'),
    'SLACK_TOKEN':      os.getenv('SLACK_TOKEN'),
    'SLACK_CHANNEL_ID': os.getenv('SLACK_CHANNEL_ID'),
    'SENDER_EMAIL':     os.getenv('SENDER_EMAIL'),
}