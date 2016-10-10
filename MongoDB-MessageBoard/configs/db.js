var mongoose = require('mongoose')

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

// Retrieve the created models for CRUD ops and make it available for use
// var User    = mongoose.model('User'),
//     Message = mongoose.model('Message'),
//     Comment = mongoose.model('Comment')
module.exports = {
  User   : mongoose.model('User'),
  Message: mongoose.model('Message'),
  Comment: mongoose.model('Comment')
}
