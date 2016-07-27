var exp = require('express')
var app = exp()

app.use(exp.static(__dirname + '/static'))

app.set('views', __dirname + '/view')
app.set('view engine', 'ejs')

app.get('/', function(req, resp){
  resp.render('index', {user: ''})
})

var server = app.listen(5000, function(){
  console.log('Server is up: loaclhost/5000')
})

var io = require('socket.io').listen(server)
var clients = []
var clientCount = 0
var socketIDMap = {}
var chat = []
var msg = {name: '', text: ''}

io.sockets.on('connection', function(serverSocket){
  console.log('Connected!', serverSocket.id)

  serverSocket.on('user_login', function(data){
    clientCount += 1
    socketIDMap[serverSocket.id] = clientCount
    clients.push({id: clientCount, name: data.name})

    serverSocket.emit('cur_user', {name: data.name})

    serverSocket.emit('all_users', {all_names: clients, all_chat: chat})

    serverSocket.broadcast.emit('new_user', {id: clientCount, name: data.name})
  })

  serverSocket.on('new_msg', function(data){
    chat.push(data)

    serverSocket.broadcast.emit('new_msg', {name: data.name, msg: data.msg})
  })

  serverSocket.on('disconnect', function(data){
    console.log('Disconnected!!', serverSocket.id)

    serverSocket.broadcast.emit('user_logoff', {id: socketIDMap[serverSocket.id]})

    for (let i = 0; i < clients.length; i++){
      if (clients[i].id == socketIDMap[serverSocket.id]){
        clients.splice(i, 1)
        break
      }
    }

    delete socketIDMap[serverSocket.id]
  })

})
