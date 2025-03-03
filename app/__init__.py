from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)
app.config.from_object(Config) 
app.secret_key = app.config['SECRET_KEY']


mail = Mail(app)  # Initialize Flask-Mail

from app import views  # Import views to avoid circular imports
