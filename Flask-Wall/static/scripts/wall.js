$(document).ready(function(){

  // This is the function to toggle the visibility of the comments panel below each message
  // This is a seperate function so that I can bind it to the dynamically introduced elements
  show_comment()

  // This is for posting messages to the wall.
  // It refreshes the entire set of messages everytime you post. ***Not very efficient***
  // The way to go would be to add only the new messages (message delta) added to the page everytime you refresh the page
  $('#in_message').submit(function(event){
    event.preventDefault()
    if ($('#in_message textarea').val().length > 0){
      $.ajax({
        type: 'post',
        url: '/in_message',
        data: $(this).serialize(),
        success: function(response){
          $('#graffitti').html(response)
          show_comment()
          $('#in_message textarea').val('')
        }
      })
    }
  })

  // This is for deleting a message on the wall
  // Again, this also refreshes the entire wall every time we try to delete. ***Not very efficient***
  // We need to track and display just the message delta
  $('.del_msg').click(function(event){
    event.preventDefault()
    var m_id = $(this)[0].id.substr(3)
    var msg_id = "msg_id="+m_id

    $(this).hide()
    $('#u'+m_id).hide()
    $('#d'+m_id).hide()

    $.ajax({
      type: 'post',
      url: '/del_message',
      data: msg_id,
      success: function(response){
        $('#graffitti').html(response)
        show_comment()
      }
    })
  })
})


// Standalone function to toggle the visibility of the comments panel below each message on the wall.
// This also handles posting of comments under the message.
// Posting comments also works in the same in-efficient way as posting messages
// Should be tracking and updating comment deltas instead of retrieving full set of comments all the time
function show_comment(){
  $('.show_cmt').click(function(event){
    event.preventDefault()
    var m_id = $(this)[0].id.substr(2)
    var msg_id = "msg_id="+m_id
    var comment_div = '#c'+m_id
    var clist_div = '#clist'+m_id

    if ($(comment_div).is(':hidden')){
      $.ajax({
        type: 'post',
        url: '/post_comment',
        data: msg_id,
        success: function(response){
          $(clist_div).html(response)
        }
      })
    }
    $(comment_div).slideToggle()
  })

  $('.send_cmt').click(function(event){
    event.preventDefault()

    var form_data = $(this).parent().serialize()
    var div_id = '#clist'+$(this).parent().parent()[0].id.substr(1)
    var parent_id = $(this).parent().parent()[0].id

    if ($('#'+parent_id+' .post_comment textarea').val().length > 0 ){
      $.ajax({
        type: 'post',
        url: '/post_comment',
        data: form_data,
        success: function(response){
          $(div_id).html(response)
          $('#'+parent_id+' .post_comment textarea').val('')
        }
      })
    }
  })
}
