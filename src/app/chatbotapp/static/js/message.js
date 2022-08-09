var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function () {

    // establish a connection with the server
    socket.emit('incoming_connection', {
        data: 'Incoming connection....'
    })

    // send user connection

    document.querySelector('#send').onclick = () => {
        var msg = document.querySelector("#usermsg").value
        socket.emit('incoming_connection', {
            'message': msg,
        });
        
        // set the user query to nill
        document.querySelector('#usermsg').value = '';
    };
})
socket.on('chatbot_response', function (msg) {
    // TODO: update the chat interface
    document.querySelector('#res').innerHTML = msg.data;
})
