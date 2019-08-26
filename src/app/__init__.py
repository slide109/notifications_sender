from flask import Flask
from flask_mail import Mail

from app.settings import app_variables

from .modules.Site import site as site_blueprint

app = Flask(__name__)

'''
  Update config
'''
app.config.update(dict(
    MAIL_SERVER   = app_variables['MAIL_SERVER'],
    MAIL_PORT     = app_variables['MAIL_PORT'],
    MAIL_USE_TLS  = app_variables['MAIL_USE_TLS'],
    MAIL_USE_SSL  = app_variables['MAIL_USE_SSL'],
    MAIL_USERNAME = app_variables['MAIL_USERNAME'],
    MAIL_PASSWORD = app_variables['MAIL_PASSWORD'],
))

'''
  Register blueprints
'''
app.register_blueprint(site_blueprint, url_prefix='/site')

'''
  Initialize Flask Mail instance
'''
mail = Mail(app)
