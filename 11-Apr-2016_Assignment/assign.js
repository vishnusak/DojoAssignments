function matchCards(){
  //this is used to access the children of the element. Each child can be individually accessed using the the ".eq(i)" method. The full list of children can be traversed using the ".each()" method
  var liElems = $('.menu').children(); 
  var cardP = $('.card').children();
  var cardColor = [];

  for (var i = 0; i < liElems.length; i++){
    for (var j = 0; j < cardP.length; j++){
      if (liElems.eq(i).text() === cardP.eq(j).text()){
        cardColor[i] = cardP.eq(j).parent().css("background-color");
        // liElems.eq(i).css("background-color", cardColor[i]);
        j = cardP.length;
      }
    }
  }
  $('.menu').data('cColor', cardColor);
}

function showItem(item){
  $('.menu li').each(function(index){
    if (index === (item)){
      $(this).show(200);
      $(this).css("background-color", $('.menu').data('cColor')[index]);
      $(this).animate({width: "12.5vw", height: "5vh"},{queue: false, duration: 300});
      $(this).promise().done(function(){
        $(this).animate({fontSize: "1.2vw"}, 30);
      })
      showPage($(this).index());
    } else {
      $(this).show(200);
      $(this).css("background-color", $('html').css("background-color"));
      $(this).animate({width: "4vw", height: "5vh"},{queue: false, duration: 300});      
    }
  })
}

function showMenu(item){
  $('.menu').show(300);
  $('.menu').animate({width: "17vw"}, {queue: false, duration: 300});
  // $('.menu').animate({fontSize: "1.2vw"}, {queue: false, duration: 300});
  $('main').animate({left: "18.5vw"}, {queue: false, duration: 300});
  $('main').animate({width: "70vw"}, {queue: false, duration: 300});
    matchCards();
    showItem(item);
}

function showPage(idx){
  $('.challenge').hide();
  var pageId = "c" + (idx+1);
  $('#' + pageId + '.challenge').show();
  $('#' + pageId + ' .fullpage').slideDown(1000);
  $('#' + pageId + ' .fullpage').css("border-color", $('.menu').data('cColor')[idx]);
  $('#' + pageId + ' .fullpage button').css("background-color", $('.menu').data('cColor')[idx]);
  $('#' + pageId + ' .fullpage p').text('');
  $('#' + pageId + ' .fullpage input').val('');
  $('#' + pageId + ' .fullpage').css("display", "block");
}

function hidePage(){
  $('.fullpage').hide();
}

function colorPicker(){
  var red   = Math.floor(Math.random() * 256);
  var green = Math.floor(Math.random() * 256);
  var blue  = Math.floor(Math.random() * 256);

  return "rgb("+red+","+green+","+blue+")";
}

$('document').ready(function(){
  $('.card').each(function(){
    var cpColor = colorPicker();
    $(this)
      .css("background-color",cpColor)
      .css("box-shadow","0vw 0.2vh 1.75vw "+cpColor);
  })

  $('.card').click(function(event){
    // console.log(event);
    // console.log(event.currentTarget.id);
    // console.log(this.id);
    $('.card').data("cardId", this.id);
    $('.card').fadeOut(400);
    $('body').animate({height: "90vh"}, 400);
    $('body').promise().done(function(){
      showMenu(Number($('.card').data("cardId").slice(2)) - 1);
      // console.log($('.card').data("cardId"));
      // switch ($('.card').data("cardId")){
      //   case 'cd1':
      //     showMenu(0);
      //     break;
      //   case 'cd2':
      //     showMenu(1);
      //     break;
      //   case 'cd3':
      //     showMenu(2);
      //     break;
      //   case 'cd4':
      //     showMenu(3);
      //     break;
      //   case 'cd5':
      //     showMenu(4);
      //     break;
      // }
    })
  })
  // $('#cd1').click(function(){
  //   $('.card').fadeOut(200);
  //   $('body').animate({height: "90vh"}, 200);
  //   $('body').promise().done(function(){
  //     showMenu(1);
  //   })
  // })

  // $('#cd2').click(function(){
  //   $('.card').fadeOut(200);
  //   $('body').animate({height: "90vh"}, 200);
  //   $('body').promise().done(function(){
  //     showMenu(2);
  //   })
  // })

  // $('#cd3').click(function(){
  //   $('.card').fadeOut(200);
  //   $('body').animate({height: "90vh"}, 200);
  //   $('body').promise().done(function(){
  //     showMenu(3);
  //   })
  // })

  // $('#cd4').click(function(){
  //   $('.card').fadeOut(200);
  //   $('body').animate({height: "90vh"}, 200);
  //   $('body').promise().done(function(){
  //     showMenu(4);
  //   })
  // })

  // $('#cd5').click(function(){
  //   $('.card').fadeOut(200);
  //   $('body').animate({height: "90vh"}, 200);
  //   $('body').promise().done(function(){
  //     showMenu(5);
  //   })
  // })

  // $('.menu li').hover(function(){
  //   $(this).addClass('menuhover');    
  // }, function(){
  //   $(this).removeClass('menuhover');
  // })

  // $('.menu li').each(function(index){
  //   $(this).hover(function(){
  //     if ($(this).css("width") !== '215px'){
  //       console.log($(this).css("width"));
  //       $(this).append("<span>"+($(this).text())+"</span>");
  //       $('.menu li span').css("left",$(this).css("width"));
  //     }
  //   }, function(){
  //     $('.menu li span').remove();
  //   })
  // })

  var bgColor = $('html').css("background-color");
  $('.menu').data("bgColor", bgColor);

  $('.menu li').hover(function(){
    if ($(this).css("background-color") === $('.menu').data("bgColor")){
      $(this).css("fontSize", "0.75vw").animate({width: "8vw"}, 300);
    }
  }, function(){
    if ($(this).css("background-color") === $('.menu').data("bgColor")){
      $(this).css("fontSize", "0vw").animate({width: "4vw"}, 300);
    }
  })


  $('.menu li').click(function(){
    if ($(this).css("background-color") === $('.menu').data("bgColor")){
      $(this).css("background-color",$('.menu').data('cColor')[$(this).index()]).css("fontSize","1.2vw").animate({width: "12.5vw"}, 300);
      $('.menu li').not(this).each(function(){
        $(this).css("fontSize", "0vw").css("background-color", $('html').css("background-color")).animate({width: "4vw"}, 300);
      })
      hidePage();
      showPage($(this).index());
    }
  })

  $('.btnlbl').children().click(function(){
    switch(this.id){
      case 'b1':
        $('#p1').text('');
        chickBoom('#p1');
        break;
      case 'b2':
        $('#p2').text('');
        $('#p2').text('The Sigma of ' + $('#inp2').val() + ' is ' + sigma(Number($('#inp2').val())));
        break;
      case 'b3':
        $('#p3').text('');
        $('#p3').text('The factorial of '+ $('#inp3').val() + ' is ' + fact(Number($('#inp3').val())));
        break;
      case 'b4':
        $('#p4').text('');
        $('#p4').text($('#inp4').val() + ' Stars on The Left: ' + drawLeftStars(Number($('#inp4').val())));
        break;
      case 'b5':
        $('#p5').text('');
        $('#p5').text($('#inp5').val() + ' Stars on The Right: ' + drawRightStars(Number($('#inp5').val())));
        break;
      case 'b6':
        $('#p6').text('');
        $('#p6').text($('#inp6').val() + ' Stars in The Centre: ' + drawCenteredStars(Number($('#inp6').val())));
        break;
      case 'b7':
        $('#p7').text('');
        $('#p7').text($('#inp71').val() + ' of ' + $('#inp72').val() +' chars in the Left: ' + drawLeftChars(Number($('#inp71').val()),$('#inp72').val()));
        break;
      case 'b8':
        $('#p8').text('');
        $('#p8').text($('#inp81').val() + ' of ' + $('#inp82').val() +' chars in the Left: ' + drawRightChars(Number($('#inp81').val()),$('#inp82').val()));
      case 'b9':
        $('#p9').text('');
        $('#p9').text($('#inp91').val() + ' of ' + $('#inp92').val() +' chars in the Left: ' + drawCenteredChars(Number($('#inp91').val()),$('#inp92').val()));
    }
    // $('#p'+(this.id).slice(1)).html('Hi There');
  })
})

function chickBoom(p){
  for (var i = 1; i <= 12; i++){
    $(p).append(i + " chick " + " boom " + " chick ");
  }
}

function sigma(num){
  if (num === 1){
    return 1;
  } else {
    return num + sigma(num - 1);
  }
}

function fact(num){
  if (num === 1){
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

function drawLeftStars(num){
  var stars = '';
  for (var i = 1; i <= num; i++){
    stars += '*';
  }
  for (var i = num + 1; i <= 75; i++){
    stars += '_';
  }
  return stars;
}

function drawRightStars(num){
  var stars = '';
  for (i = 1; i <= 75-num; i++){
    stars += '_';
  }
  for (var i = stars.length; i <= 75; i++){
    stars += '*';
  }
  return stars;
}

function drawCenteredStars(num){
  var stars = '';
  for (var i = 1; i <= Math.floor(37-(num/2)); i++){
    stars += '_';
  }
  for (var i = 1; i <= num; i++){
    stars += '*';
  }
  for (var i = stars.length; i <= 75; i++){
    stars += '_';
  }
  return stars;
}

function drawLeftChars(num, char){
  var stars = '';
  for (i = 1; i <= num; i++){
    stars += char;
  }
  for (var i = num + 1; i <= 75; i++){
    stars += '_';
  }
  return stars;
}

function drawRightChars(num, char){
  var stars = '';
  for (i = 1; i <= 75-num; i++){
    stars += '_';
  }
  for (var i = stars.length; i <= 75; i++){
    stars += char;
  }
  return stars;
}

function drawCenteredChars(num, char){
  var stars = '';
  for (var i = 1; i <= 37-(num/2); i++){
    stars += '_';
  }
  for (var i = 1; i <= num; i++){
    stars += char;
  }
  for (var i = stars.length; i <= 75; i++){
    stars += '_';
  }
  return stars;
}