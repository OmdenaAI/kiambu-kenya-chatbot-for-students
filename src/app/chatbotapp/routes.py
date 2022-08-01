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
def handle_incoming_connection(data, methods=['GET', 'POST']):
    """This is the chat client that listens to incoming message and 
        send back resposne to the chat client
    """

    #TODO: Complete the application and add user request parsing and sending the models response
    #extract the application
    incoming_message = data.get("message", "")

    chat_res = Util.process_input(incoming_message)
    
    print(f'received my message from front end client: {incoming_message}')

    #call the predict method and get response
    res = {
        "data": chat_res
    }

    #send the response back to the user
    socketio.emit('chatbot_response', res, callback=Util.incoming_event_callback)
