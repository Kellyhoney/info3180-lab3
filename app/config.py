import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', '18500f5e3ac327691b34bf4ef4c75b23beb6b8085aec7d00')

    # Flask-Mail Configuration (Mailtrap)
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'sandbox.smtp.mailtrap.io')  
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 2525))  
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'b11c799e082117')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '01d28c1671a383')

    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() == 'true'  
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False').lower() == 'true'  



