$('document').ready(function(){
  $('img').click(function(){
    // $(this).hide();
    $(this).animate({'opacity': '0'}, 1000);
  })

  $('button').click(function(){
    // $('img').show();
    $('img').animate({'opacity': '1'},200);
  })
})