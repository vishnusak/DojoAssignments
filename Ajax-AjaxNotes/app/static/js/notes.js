$(document).ready(function(){
// ------------------------------------------------------------------
  showform()
// ------------------------------------------------------------------
  $('form').submit(function(e){

    e.preventDefault()
    var data = $(this).serialize()
    if (data.split('=')[1]){
      $.ajax({
        method: 'POST',
        url: '/notes/add',
        data: data,
        success: function(resp){
          $('.left').html(resp)
          $('form').trigger('reset')
          $('.right').hide()
        }
      })
    }

  })

// ------------------------------------------------------------------
  $('.left').on('click', '.delete', function(){

    $.ajax({
      method: 'GET',
      url: '/notes/del/'+this.id,
      success: function(resp){
        $('.left').html(resp)
        showform()
      }
    })

  })

// ------------------------------------------------------------------
  $('.left').on('click', '.add', function(){

    $('.right').show()

  })

// ------------------------------------------------------------------
  var clicked_id = ''
  var clicked_text = ''

  $('.left').on('click', '.text', function(){

    clicked_id = this.id
    clicked_text = $(this)[0]['innerHTML']
    var ro = $('#'+this.id).prop('readonly')
    $('#'+this.id).attr('readonly', !ro).css({"background": "white"})

  }).on('focusout', '.text', function(){
    if (clicked_id == this.id){
      if (clicked_text != $(this)[0]['value']){
        $.ajax({
          method: 'POST',
          url: '/notes/update/'+this.id.substr(1),
          data: 'note='+$(this)[0]['value'],
          success: function(resp){
            $('.left').html(resp)
          }
        })
        clicked_id = ''
        clicked_text = ''
      }
    }

  })
// ------------------------------------------------------------------

})

function showform(){
  if ($('.note').length == 0){
    $('.right').hide()
    $('.right').show()
  }
}
