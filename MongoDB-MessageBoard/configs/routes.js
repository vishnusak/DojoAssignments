var formValidations = require('./formValidations'),
    bcrypt          = require('bcrypt'),
    session         = require('express-session'),
    parser          = require('body-parser'),
    db              = require('./db')

module.exports = function(app){
  app.use(parser.urlencoded({extended: true}))
  // Set up the app for using session
  app.use(session({
    secret: 'sjdfniu28e2ndco83uxq8o~(WnE98j*2qebd%$^&giuygfdfh',
    resave: true,
    saveUninitialized: false
  }))

  return {
    index: function(req, res){
      if (!req.session.name){ req.session.name = '' }
      if (!req.session.errors){
        req.session.errors = { start: true, login: false, register: false, fname: '', lname: '', email: '', password: '', cpassword: '', inpfname: '', inplname: '', inpemail: '', inppwd: '', inpcpwd: '' }
      }

      res.render('index', req.session.errors)
    },

    signout: function(req, res){
      req.session.destroy()

      res.redirect('/')
    },

    register: function(req, res){

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
          fName             = formValidations.validateName(inpData.fname)
          req.session.errors.inpfname = inpData.fname
          break
          case 'lname':
          lName             = formValidations.validateName(inpData.lname)
          req.session.errors.inplname = inpData.lname
          break
          case 'email':
          eMail             = formValidations.validateMail(inpData.email)
          req.session.errors.inpemail = inpData.email
          break
          case 'password':
          passWord          = formValidations.validatePwd(inpData.password)
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
        var user      = new db.User()
        user.fname    = inpData.fname
        user.lname    = inpData.lname
        user.email    = inpData.email
        user.password = bcrypt.hashSync(inpData.password, 10)

        user.save(function(err, user){
          if (err){
            console.log(`Error on User insert. Error is ${err}`)
          } else {
            req.session.name   = user.fname
            db.Message.find({}).populate('comments').exec(function(err, msgData){
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
    },

    login: function(req, res){

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
        db.User.findOne({email: inpData.email}, function(err, data){
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
                db.Message.find({}).populate('comments').exec(function(err, msgData){
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
    },

    postMessage: function(formData, serverSocket, io){
      var msg = new db.Message()
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
    },

    postComment: function(formData, serverSocket, io){
      var cmt = new db.Comment()
      cmt.name= formData.name
      cmt.cmtText = formData.cmtText
      cmt._message= formData.msgId

      db.Message.findOne({_id: formData.msgId}, function(err, msg){
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
    },

    disconnect: function(id){
      console.log('disconnected', id)
    }
  }
}
