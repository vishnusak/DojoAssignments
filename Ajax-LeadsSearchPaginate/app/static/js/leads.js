$(document).ready(function(){
  // ---------------------------------------------------------------------
  $('ul').on('click', 'li', function(){

    $.ajax({
      method: 'POST',
      url: '/leads/'+this.id,
      data: $('form').serialize(),
      dataType: 'json',
      success: function(resp){
        $('ul').html(resp['page'])
        $('tbody').html(resp['details'])
      }
    })

  })
  // ---------------------------------------------------------------------
  timer_id_name = ''
  // $('#name').keypress(function(e){
  $('#name').keydown(function(e){
    // A-Z: 65-90
    // 0-9: 48-57 / 96-105
    // console.log($('#name').val()+e['key'])
    if (timer_id_name){
      clearTimeout(timer_id_name)
      timer_id_name = ''
    }
    timer_id_name = setTimeout(post_req, 500)
  })
  // ---------------------------------------------------------------------

  $("#from").change(post_req)
  // ---------------------------------------------------------------------

  $("#to").change(post_req)
  // ---------------------------------------------------------------------
})

// ---------------------------------------------------------------------
function post_req(){

  timer_id_name = ''
  $.ajax({
    method: 'POST',
    url: '/leads/filter',
    data: $('form').serialize(),
    success: function(resp){
      $('ul').html(resp['page'])
      $('tbody').html(resp['details'])
    }
  })

}
// ---------------------------------------------------------------------
