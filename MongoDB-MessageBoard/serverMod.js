var express = require('express'),
    socket  = require('socket.io')

// Express app
var app = express()
// Set up the static folder path
app.use(express.static(__dirname + '/static'))
// Set up the rendering engine and location for views
app.set('views', __dirname + '/views')
app.set('view engine', 'ejs')

// ----------------------------------------------------------------------

// everything related to mongoose db connection and schema creation, moved to configs/db.js
// All form validation functions moved to configs/formValidations.js
// All route callbacks moved to configs/routes.js
var routes = require('./configs/routes')(app)

app.get('/signout', routes.signout)
app.get('/', routes.index)
app.post('/register', routes.register)
app.post('/login', routes.login)

// Remember: set up passwords with Uppercase of firstname, full last name in lowercase, '$' sign and number '1' so that I don't forget later when I come back to this app.

// ----------------------------------------------------------------------
// Start the server
var server = app.listen(5000, function(){
  console.log("Message Board Server is up and running --> http://localhost/5000")
}),
// Setup the socket connection. After the login, message board will work on sockets
    io     = socket.listen(server)

io.sockets.on('connection', function(serverSocket){
  console.log('connected', serverSocket.id)

  serverSocket.on('post-message', function(formData){
    routes.postMessage(formData, serverSocket, io)
  })

  serverSocket.on('post-comment', function(formData){
    routes.postComment(formData, serverSocket, io)
  })

  serverSocket.on('disconnect', function(){
    routes.disconnect(serverSocket.id)
  })
})

// ----------------------------------------------------------------------
