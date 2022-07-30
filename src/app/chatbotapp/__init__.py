import os
#from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO

#load_dotenv()

app = Flask(__name__)
#app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

#app.config['SECRET_KEY'] = 'Myswebwkjbejber'

socketio = SocketIO(app)

from chatbotapp import routes
