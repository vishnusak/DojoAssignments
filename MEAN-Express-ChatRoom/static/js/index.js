$(document).ready(function(){
  var clientSocket = io.connect()
  var curUser = ''

  // handle 'cur_user' event. This is fired first time a user joins the chat
  clientSocket.on('cur_user', function(resp){
    $('main').show()

    $('#cur_user').text(resp.name + ':')
    curUser = resp.name

  })

  // handle 'all_users' event. This is fired first time a user joins the chat
  clientSocket.on('all_users', function(resp){
    var allUsers = resp.all_names
    var allChat = resp.all_chat

    for (let i = 0; i < allUsers.length; i++){
      showUser(allUsers[i].name, allUsers[i].id)
    }

    for (let i = 0; i < allChat.length; i++){
      showChatMsg(allChat[i].name, allChat[i].msg)
    }

  })

  // Handle 'new_user' event. This is fired every time someother user joins the chat
  clientSocket.on('new_user', function(resp){
    showUser(resp.name, resp.id)
  })

  // handle 'new_msg' event. This is fired everytime someother user posts a message in the chatroom
  clientSocket.on('new_msg', function(resp){
    showChatMsg(resp.name, resp.msg)
  })

  // hanlde 'user_logoff' event. This is fired everytime someother users leaves the chat
  clientSocket.on('user_logoff', function(resp){
    $('#' + resp.id).fadeOut('slow', function(){
      $(this).remove()
    })
  })

  // Hide the main chat window on initial page load
  $('main').hide()

  $('#cancel').click(function(e){
    e.preventDefault()
    e.stopPropagation()
    console.log("cancel");
  })

  $('#login').submit(function(e){
    e.preventDefault()
    var formData = $(this).serializeArray()

    if (formData[0].value){
      clientSocket.emit('user_login', {name: formData[0].value})
      $(this).hide()
    }

  })

  $('#text').submit(function(e){
    e.preventDefault()

    var chatMsg = $(this).serializeArray()

    if (chatMsg[0].value){
      showChatMsg(curUser, chatMsg[0].value)

      clientSocket.emit('new_msg', {name: curUser, msg: chatMsg[0].value})
      $('#text').trigger('reset')
    }

  })

})

function showChatMsg(name, msg){
  var em = document.createElement('em')
  var emText = document.createTextNode(name + ': ')
  em.appendChild(emText)
  var p1 = document.createElement('p')
  p1.appendChild(em)
  var p1Text = document.createTextNode(msg)
  p1.appendChild(p1Text)
  var p2 = document.createElement('p')
  var p2Text = document.createTextNode('...')
  p2.appendChild(p2Text)
  $('#history').append(p1)
  $('#history').append(p2)
}

function showUser(name, id){
  var p = document.createElement('p')
  var pText = document.createTextNode(name)
  p.id = id
  p.appendChild(pText)
  $('#users').append(p)
  $('#'+id).hide().fadeIn('slow')
}
