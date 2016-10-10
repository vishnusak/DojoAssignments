// Validation routines for login / register form entries

module.exports = {
  validateName: function(name){
    var length = new RegExp("^[a-zA-Z]\\w{4,14}$")
    return length.test(name)
  },

  validateMail: function(email){
    var mailPattern = new RegExp("^\\w+(\\.?\\w+)*@{1}\\w+\\.{1}\\w+(\\.?\\w+)*$"),
    isValid = mailPattern.exec(email)

    if (!isValid){
      return false
    } else if (isValid[0] !== isValid.input){
      return false
    } else {
      return true
    }
  },

  validatePwd: function(pwd){
    var pwdLength = new RegExp("^.{8,}$"),
    hasSplChar= new RegExp("[$#%@&!~]+"),
    hasUpper  = new RegExp("[A-Z]+"),
    hasDigit  = new RegExp("[0-9]+")

    return (pwdLength.test(pwd) && hasSplChar.test(pwd) && hasUpper.test(pwd) && hasDigit.test(pwd))
  }
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
