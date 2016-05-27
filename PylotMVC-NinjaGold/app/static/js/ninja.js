$(document).ready(function(){
  $('form').submit(function(e){
    e.preventDefault()
    var id = $(this)[0].id
    var process_url = `/process_money/${id}`
    $.ajax({
      method: 'POST',
      url: `${process_url}`,
      dataType: 'json',
      success: function(response){
        var activity = `<p class=${response['color']}>${response['msg']} (${response['time']})</p>`
        $('.activity').prepend(activity)
        $('#showscore').text(response['score'])
      }
    })
  })
})
