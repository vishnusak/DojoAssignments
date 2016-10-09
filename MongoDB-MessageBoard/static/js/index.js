$(document).ready(function(){

  $('#signin').click(function(){
    if ($('img').is(':visible')){
      $('img').fadeOut(500, function(){
        $('#login-form').fadeIn()
      })
    } else if ($('#register-form').is(':visible')){
      $('#register-form').fadeOut(500, function(){
        $('#login-form').fadeIn()
      })
    }
  })

  $('#signup').click(function(){
    if ($('img').is(':visible')){
      $('img').fadeOut(500, function(){
        $('#register-form').fadeIn()
      })
    } else if ($('#login-form').is(':visible')){
      $('#login-form').fadeOut(500, function(){
        $('#register-form').fadeIn()
      })
    }
  })
})
