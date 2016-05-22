$(document).ready(function(){

  // These arrays act as flags for tracking validation in the login and registration screens
  var login_err = [0, 0]
  var register_err = [0, 0, 0, 0, 0]

  // Animation to show the registration screen
  $('#goto').click(function(){
    $('#log').animate({width: 0}, 100, function(){
      $('#log').hide()
      $('#reg').show().animate({width: '100%'}, 100)
    })
  })

  // Form data validations: I believe it is much better to handle validations on the client-side/front-end of the application to make it faster and reduce traffic
  // The best way I could think of capturing the content is using the blur() / focusout() event for the text fields. The user experience is somewhere between bad and great.
  // The submit buttons are disabled till all the fields are validated correctly, but this means that on the last input field, the user has to hit the tab key to trigger the focuout event. Still trying to figure this out
  $('input[type="text"]').blur(function(){
    var element_name = $(this)[0].name
    var element_value = $(this).val()
    var element_parent = $(this).parent()[0].id

    switch (true){
      case (element_name == 'fname'):
        var isValid = name_validate(element_value)
        if (typeof isValid == "string"){
          $('#fn_err span').text(isValid)
          // $(this).select()
        } else {
          $('#fn_err span').text('')
          register_err[0] = 1
          if (register_err.reduce(function(x,y){return x+y}) == 5){
            $('#register input[type="submit"]').prop("disabled", false)
          }
        }
        break

      case (element_name == 'lname'):
        var isValid = name_validate(element_value)
        if (typeof isValid == "string"){
          $('#ln_err span').text(isValid)
          // $(this).select()
        } else {
          $('#ln_err span').text('')
          register_err[1] = 1
          if (register_err.reduce(function(x,y){return x+y}) == 5){
            $('#register input[type="submit"]').prop("disabled", false)
          }
        }
        break

      case (element_name == 'email'):
        var isValid = email_validate(element_value)
        if (element_parent == "login"){
          if (typeof isValid == "string"){
            $('#eml_err span').text(isValid)
            // $(this).select()
          } else {
            $('#eml_err span').text('')
            login_err[0] = 1
            if (login_err.reduce(function(x,y){return x+y}) == 2){
              $('#login input[type="submit"]').prop("disabled", false)
            }
          }
        } else {
          if (typeof isValid == "string"){
            $('#em_err span').text(isValid)
            // $(this).select()
          } else {
            $('#em_err span').text('')
            register_err[2] = 1
            if (register_err.reduce(function(x,y){return x+y}) == 5){
              $('#register input[type="submit"]').prop("disabled", false)
            }
          }
        }
        break
    }
  })

  $('input[type="password"]').blur(function(){
    var element_name = $(this)[0].name
    var element_value = $(this).val()
    var element_parent = $(this).parent()[0].id

    switch (true){
      case (element_name == 'password'):
        var isValid = pwd_validate(element_value)
        if (element_parent == "login"){
          if (typeof isValid == "string"){
            $('#pass_err span').text(isValid)
            // $(this).select()
          } else {
            $('#pass_err span').text('')
            login_err[1] = 1
            if (login_err.reduce(function(x,y){return x+y}) == 2){
              $('#login input[type="submit"]').prop("disabled", false)
            }
          }
        } else {
          if (typeof isValid == "string"){
            $('#pwd_err span').text(isValid)
            // $(this).select()
          } else {
            $('#pwd_err span').text('')
            register_err[3] = 1
            if (register_err.reduce(function(x,y){return x+y}) == 5){
              $('#register input[type="submit"]').prop("disabled", false)
            }
          }
        }
        break

      case (element_name == 'password_c'):
        if ($('#reg_pwd').val() != element_value){
          $('#pwdc_err span').text("PASSWORD mismatch")
          // $(this).select()
        } else {
          $('#pwdc_err span').text('')
          register_err[4] = 1
          if (register_err.reduce(function(x,y){return x+y}) == 5){
            $('#register input[type="submit"]').prop("disabled", false)
          }
        }
        break

    }
  })

})

// functions for name validation
function name_validate(name){
  var name_regex = new RegExp(/[0-9]/g)
  var num_in_name = name_regex.test(name)

  switch (true){
    case (name.length == 0):
      return "NAME is required"
    case (name.length <= 2):
      return "NAME must be more than 2 characters"
    case num_in_name:
      return "NAME is not valid. Must not have numbers"
    default:
      return true
  }
}

// functions for name validation
function email_validate(email){
  var email_regex = new RegExp(/[a-zA-Z0-9\._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+/g)
  var email_is_valid = email_regex.exec(email)

  switch (true){
    case (email.length == 0):
      return "EMAIL is required"
    case (!email_is_valid):
      return "Invalid EMAIL id"
    default:
      if (email != email_is_valid[0]){
        return "Invalid EMAIL id"
      } else {
        return true
      }
  }
}

// functions for name validation
function pwd_validate(pwd){
  var pwd_digit_regex = new RegExp(/[0-9]/g)
  var pwd_has_digit = pwd_digit_regex.test(pwd)
  var pwd_Upper_regex = new RegExp(/[A-Z]/g)
  var pwd_has_Upper = pwd_Upper_regex.test(pwd)

  switch (true){
    case (pwd.length == 0):
      return "PASSWORD is required"
    case (pwd.length < 8):
      return "PASSWORD must have atleast 8 characters"
    case (!pwd_has_digit):
      return "PASSWORD must have atleast 1 number"
    case (!pwd_has_Upper):
      return "PASSWORD must have atleast 1 capital letter"
    default:
      return true
  }
}
