$(document).ready(function(){

  $.ajax({
    method: 'GET',
    url: '/courses/load',
    dataType: 'json',
    success: function(resp){
      showall(resp)
    }
  })

  $('.addCourse').submit(function(event){
    event.preventDefault()
    switch (true){
      case ($('#name').val() == ''):
      $('#err').text("Name can't be empty")
        break
      case ($('#name').val().length < 15):
        $('#err').text("Name has to be atleast 15 chars")
        break
      default:
        $('#err').text('')

        $.ajax({
          method: 'POST',
          url: '/courses/add',
          data: $(this).serialize(),
          dataType: 'json',
          success: function(resp){
            // for (var i = 0; i < resp.length; i++){
            //   var line = `<tr><td>${resp[i]['title']}</td><td>${resp[i]['description']}</td><td>${resp[i]['created_at']}</td><td><a href='/courses/destroy/${resp[i]['id']}'>remove</a></td></tr>`
            //   $('.courselist>table>tbody').append(line)
            // }
            showall(resp)
            $('.addCourse').trigger('reset')
          }
        })
    }
  })
})

function showall(resp){
  for (var i = 0; i < resp.length; i++){
    var line = `<tr><td>${resp[i]['title']}</td><td>${resp[i]['description']}</td><td>${resp[i]['created']}</td><td><a href='/courses/destroy/${resp[i]['id']}'>remove</a></td></tr>`
    $('.courselist>table>tbody').append(line)
  }
}
