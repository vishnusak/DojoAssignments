$(document).ready(function(){
  // --------------------------------------------------------------------

  $(document)
    .ajaxStart(function(){
      $('.wait').show()
    })
    .ajaxStop(function(){
      $('.wait').hide()
    })

  // --------------------------------------------------------------------

  $('form').submit(function(e){
    e.preventDefault()
    if ($('.artist').val()){
      $.ajax({
        method: 'POST',
        url: '/tunes/'+$('.artist').val(),
        dataType: 'json',
        success: function(resp){
          if (resp['resultCount'] > 0){
            element = '<video controls autoplay src="'
            element += resp['results'][0]['previewUrl']
            element += '" />'
            $('.video').html(element)
          }
        }
      })
    }
  })

  // --------------------------------------------------------------------

  // $('form').submit(function(e){
  //   e.preventDefault()
  //   if ($('.artist').val()){
  //     $.ajax({
  //       method: 'POST',
  //       url: "https://itunes.apple.com/search?term="+$('.artist').val()+"&entity=musicVideo",
  //       dataType: 'jsonp',
  //       success: function(resp){
  //         if (resp['resultCount'] > 0){
  //           element = '<video controls autoplay src="'
  //           element += resp['results'][0]['previewUrl']
  //           element += '" />'
  //           $('.video').html(element)
  //           $('form').trigger('reset')
  //         }
  //       }
  //     })
  //   }
  // })
  //
  // --------------------------------------------------------------------


})
