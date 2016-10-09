var express = require('express'),
    bcrypt  = require('bcrypt'),
    parser  = require('body-parser'),
    mongoose= require('mongoose'),
    session = require('express-session'),
    socket  = require('socket.io')

// Express app
var app = express()
// Set up the app for using session
app.use(session({
  secret: 'sjdfniu28e2ndco83uxq8o~(WnE98j*2qebd%$^&giuygfdfh',
  resave: true,
  saveUninitialized: false
}))
// Set up the static folder path
app.use(express.static(__dirname + '/static'))
app.use(parser.urlencoded({extended: true}))
// Set up the rendering engine and location for views
app.set('views', __dirname + '/views')
app.set('view engine', 'ejs')

// MongoDB connection
mongoose.connect('mongodb://localhost/messageBoard')

// MongoDB schema and model details
var schema = mongoose.Schema

// User schema to hold the registered users and check during login
var userSchema = new schema({
  fname:    {type: String, required: true, minlength: 5, maxlength: 15},
  lname:    {type: String, required: true, minlength: 5, maxlength: 15},
  email:    {type: String, required: true},
  password: {type: String, required: true}
})

// Messsage schema to hold the user name and the message text and association to the comment schema. Association is via the comment ID
var msgSchema = new schema({
  name:     {type: String, required: true},
  msgText:  {type: String, required: true},
  comments: [{type: schema.Types.ObjectId, ref: 'Comment'}]
},
{timestamps:{
  createdAt: 'created_at',
  updatedAt: 'updated_at'
}})

// Comment schema to hold the user name and comment text and the association back to Message schema. The association is via the message ID
var cmtSchema = new schema({
  _message:   {type: schema.Types.ObjectId, ref: 'Message'},
  name:    {type: String, required: true},
  cmtText: {type: String, required: true}
},
{timestamps: {
  createdAt: 'created_at',
  updatedAt: 'updated_at'
}})

// Create the models from the schemas. The collection in MongoDb will have the same name as the model but in plural -> messages, comments, users
mongoose.model('User', userSchema)
mongoose.model('Message', msgSchema)
mongoose.model('Comment', cmtSchema)

// Retrieve the created models for CRUD ops
var User    = mongoose.model('User'),
    Message = mongoose.model('Message'),
    Comment = mongoose.model('Comment')

// Validation routines for login / register form entries
function validateName(name){
  var length = new RegExp("^[a-zA-Z]\\w{4,14}$")
  return length.test(name)
}

function validateMail(email){
  var mailPattern = new RegExp("^\\w+(\\.?\\w+)*@{1}\\w+\\.{1}\\w+(\\.?\\w+)*$"),
  isValid = mailPattern.exec(email)

  if (!isValid){
    return false
  } else if (isValid[0] !== isValid.input){
    return false
  } else {
    return true
  }
}

function validatePwd(pwd){
  var pwdLength = new RegExp("^.{8,}$"),
  hasSplChar= new RegExp("[$#%@&!~]+"),
  hasUpper  = new RegExp("[A-Z]+"),
  hasDigit  = new RegExp("[0-9]+")

  return (pwdLength.test(pwd) && hasSplChar.test(pwd) && hasUpper.test(pwd) && hasDigit.test(pwd))
}

// Function to convert serialized form data into an ObjectId
// Redundant now that I am getting the data directly instead of sockets.
// function jsonifySerialize(formInput){
//   var pairs = formInput.split('&'),
//       inputAsJSON = {}
//
//   for (let idx in pairs){
//     let keyValue = pairs[idx].split('=')
//     inputAsJSON[keyValue[0]] = keyValue[1].replace(/%40/, '@')
//   }
//
//   return inputAsJSON
// }

// Setup the /signout route
app.get('/signout', function(req, res){
  req.session.destroy()

  res.redirect('/')
})

// Setup the base route and the session vars
app.get('/', function(req, res){
  if (!req.session.name){ req.session.name = '' }
  if (!req.session.errors){
    req.session.errors = { start: true, login: false, register: false, fname: '', lname: '', email: '', password: '', cpassword: '', inpfname: '', inplname: '', inpemail: '', inppwd: '', inpcpwd: '' }
  }

  res.render('index', req.session.errors)
})

// Remember: set up passwords with Uppercase of firstname, full last name in lowercase, '$' sign and number '1' so that I don't forget later when I come back to this app.
// Setup the /register route
app.post('/register', function(req, res){

  var inpData  = req.body,
      fName    = false,
      lName    = false,
      eMail    = false,
      passWord = false,
      cpassWord= false,
      errFlag  = false

  for (key in req.session.errors){
    req.session.errors[key] = ''
  }

  req.session.errors.start    = false
  req.session.errors.login    = false
  req.session.errors.register = true

  for (let key in inpData){
    switch (key){
      case 'fname':
        fName             = validateName(inpData.fname)
        req.session.errors.inpfname = inpData.fname
        break
      case 'lname':
        lName             = validateName(inpData.lname)
        req.session.errors.inplname = inpData.lname
        break
      case 'email':
        eMail             = validateMail(inpData.email)
        req.session.errors.inpemail = inpData.email
        break
      case 'password':
        passWord          = validatePwd(inpData.password)
        req.session.errors.inppwd   = inpData.password
        break
      case 'c_password':
        cpassWord         = (inpData.c_password == inpData.password)
        req.session.errors.inpcpwd  = inpData.c_password
        break
    }
  }

  if (!fName){
    errFlag = true
    req.session.errors['fname'] = "Invalid entry. Should have atleast 5 characters"
  }

  if (!lName){
    errFlag = true
    req.session.errors['lname'] = "Invalid entry. Should have atleast 5 characters"
  }

  if (!eMail){
    errFlag = true
    req.session.errors['email'] = "Invalid email address"
  }

  if (!passWord){
    errFlag = true
    req.session.errors['password'] = "Should be minimum 8 chars long with atleast 1 uppercase char, 1 lowercase char, 1 special char and 1 number"
  }

  if (!cpassWord){
    errFlag = true
    req.session.errors['cpassword'] = "Password mismatch. Type the same password as above."
  }

  if (errFlag){
    res.redirect('/')
  } else {
    // add new row in user db
    var user      = new User()
    user.fname    = inpData.fname
    user.lname    = inpData.lname
    user.email    = inpData.email
    user.password = bcrypt.hashSync(inpData.password, 10)

    user.save(function(err, user){
      if (err){
        console.log(`Error on User insert. Error is ${err}`)
      } else {
        req.session.name   = user.fname
        Message.find({}).populate('comments').exec(function(err, msgData){
          if (err){
            console.log("Unable to retrieve messages: ", err)
            req.session.errors['fname'] = "Unable to register now. Try later"
            res.redirect('/')
          } else {
            res.render('message', {user: req.session.name, messages: msgData})
          }
        })
      }
    })
  }
})

// Set up the /login route
app.post('/login', function(req, res){

  var inpData  = req.body,
      eMail    = false,
      passWord = false,
      errFlag  = false

  for (key in req.session.errors){
    req.session.errors[key] = ''
  }

  req.session.errors.start    = false
  req.session.errors.login    = true
  req.session.errors.register = false

  for (let key in inpData){
    switch (key){
      case 'email':
        if (inpData.email){ eMail = true }
        req.session.errors.inpemail = inpData.email
        break
      case 'password':
        if (inpData.password){ passWord = true }
        req.session.errors.inppwd   = inpData.password
        break
    }
  }

  if (!eMail){
    errFlag = true
    req.session.errors['email'] = "email address is required"
  }

  if (!passWord){
    errFlag = true
    req.session.errors['password'] = "password is required"
  }

  if (errFlag){
    res.redirect('/')
  } else {
    // check user in db
    User.findOne({email: inpData.email}, function(err, data){
      if (err){
        console.log("Error in reading users table: ", err)
        req.session.errors['email'] = "Unable to login now. Try later"
        res.redirect('/')
      } else {
        // Check if some data has been retrieved from the table for the given email id.
        if (data){
          // check the password retrieved from table against the user provided password
          if (bcrypt.compareSync(inpData.password, data.password)){
            req.session.name   = data.fname
            Message.find({}).populate('comments').exec(function(err, msgData){
              if (err){
                console.log("Unable to retrieve messages: ", err)
                req.session.errors['email'] = "Unable to login now. Try later"
                res.redirect('/')
              } else {
                res.render('message', {user: req.session.name, messages: msgData})
              }
            })
          } else {
            // Password provided in login page doesn't match password from db
            req.session.errors['password'] = "password mismatch"
            res.redirect('/')
          }
        } else {
          // The provided email id didn't retrieve any data from the table.
          req.session.errors['email'] = "email not found"
          res.redirect('/')
        }
      }
    })
  }
})

// Start the server
var server = app.listen(5000, function(){
  console.log("Message Board Server is up and running --> http://localhost/5000")
}),
// Setup the socket connection. After the login, message board will work on sockets
    io     = socket.listen(server)

io.sockets.on('connection', function(serverSocket){
  console.log('connected', serverSocket.id)

  serverSocket.on('post-message', function(formData){
    var msg = new Message()
    msg.name= formData.name
    msg.msgText= formData.msgText

    msg.save(function(err, msg){
      if (err){
        console.log("Error while saving message: ", err)
      } else {
        formData.msgId = msg._id
        io.emit('new-message', formData)
      }
    })
  })

  serverSocket.on('post-comment', function(formData){
    var cmt = new Comment()
    cmt.name= formData.name
    cmt.cmtText = formData.cmtText
    cmt._message= formData.msgId

    Message.findOne({_id: formData.msgId}, function(err, msg){
      msg.comments.push(cmt)
      cmt.save(function(err){
        if (err){
          console.log("Unable to save comment: ", err)
        } else {
          msg.save(function(err){
            if (err){
              console.log("Unable to update message: ", err)
            } else {
              io.emit('new-comment', formData)
            }
          })
        }
      })
    })
  })

  serverSocket.on('disconnect', function(){
    console.log('disconnected', serverSocket.id)
  })
})
