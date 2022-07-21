from datetime import date
from flask import render_template, url_for, flash, redirect, request
from chatbotapp.forms import ChatForm
from chatbotapp.utils import Util
from chatbotapp import app, socketio


@app.route("/", methods=['GET', 'POST'])
def index():
    """This is the default view function, it returns a chat menu that the client can use to enter queries.
        """
    return render_template('index.html')


@socketio.on('incoming_connection')
def handle_incoming_connection(json, methods=['GET', 'POST']):
    """This is the chat client that listens to incoming message and 
        send back resposne to the chat client
    """

    #TODO: Complete the application and add user request parsing and sending the models response
    print(f'received my message from front end client: {str(json)}')
    socketio.emit('chatbot_response', json, callback=Util.incoming_event_callback)