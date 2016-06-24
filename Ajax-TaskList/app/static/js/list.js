$(document).ready(function(){
  // ------------------------------------------------------------
  $('.add').submit(function(e){
    e.preventDefault()
    var data = $(this).serialize().split('=')
    if (data[1].length > 0){
      $.ajax({
        method: 'POST',
        url: '/tasks/add',
        data: $(this).serialize(),
        success: function(resp){
          $('.list').html(resp)
          $('.add').trigger('reset')
        }
      })
    }
  })
  // ------------------------------------------------------------
  var orig_task = ''
  $('.list').on('submit', '.tasklist', function(e){
    e.preventDefault()

    var this_id = $(this).attr('id')
    var this_button_txt = $("#"+this_id+" input[type='submit']").val()
    var ro = $("#"+this_id+" input[type='text']").attr('readonly')

    if (this_button_txt == 'Edit'){

      $("#"+this_id+" input[type='submit']")
        .val('Save')
      $("#"+this_id+" input[type='text']")
        .attr('readonly', !ro)
        .css({"border": "1px solid black", "background": "lightgreen"})
        .focus()
      orig_task = $(this).serialize()

    } else {

      $("#"+this_id+" input[type='submit']")
        .val('Edit')
      $("#"+this_id+" input[type='text']")
        .attr('readonly', !ro)
        .css({"border": "none", "background": "none"})

      if (orig_task != $(this).serialize()){
        $.ajax({
          method: 'POST',
          url: '/tasks/update/'+this_id,
          data: $(this).serialize(),
          success: function(resp){
            $('.list').html(resp)
          }
        })
      }

    }
  })
  // ------------------------------------------------------------
  // $("input[type='checkbox']").click(function(){
  $('.list').on('click', "input[type='checkbox']", function(){
    if ($(this)[0]['checked']){
      $.ajax({
        method: 'POST',
        url: '/tasks/delete/'+this.id,
        success: function(resp){
          $('.list').html(resp)
        }
      })
    }
  })
  // ------------------------------------------------------------
})
