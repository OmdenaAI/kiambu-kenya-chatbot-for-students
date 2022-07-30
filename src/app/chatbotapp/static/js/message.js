var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', function () {

    // establish a connection with the server
    socket.emit('incoming_connection', {
        data: 'Incoming connection....'
    })

    // send user connection

    socket.emit('incoming_connection', {
        // TODO: Capture user input and send back a response
        message: "How do I enroll to a Masters program in the University?"
    })
})
socket.on('chatbot_response', function (msg) {
    console.log("some chatbot event")
    console.log(msg)

    // TODO: update the chat interface
})
