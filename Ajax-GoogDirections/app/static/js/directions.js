$(document).ready(function(){
  // ----------------------------------------------------------------------
  // $('form').submit(function(e){
  //   e.preventDefault()
  //   console.log($(this).serialize())
  //   goog_url = "https://maps.googleapis.com/maps/api/directions/json?"+$(this).serialize()+"&key=AIzaSyC6DTLmwYaTG6KRcVxY4gt56ZeVwRrNN-4"
  //   $.ajax({
  //     method: 'GET',
  //     url: goog_url,
  //     dataType: 'jsonp',
  //     success: function(resp){
  //       console.log(resp['geocoded_waypoints'])
  //       console.log(typeof resp)
  //     }
  //   })
  // })
  // ----------------------------------------------------------------------
  $('form').submit(function(e){
    e.preventDefault()
    $.ajax({
      method: 'POST',
      url: '/directions',
      data: $(this).serialize(),
      success: function(resp){
        $('.directions').html(resp)
      }
    })
    $('form').trigger('reset')
  })

  // ----------------------------------------------------------------------

})
