function putCard(fd){
  var divStart = "<div class='ccards'>";
  var h1Line   = "<h1>" + fd.fn + " " + fd.ln + "</h1>";
  var pLine    = "<p><em>Click for Description</em></p>";
  var descLine = "<p class='desc'>" + fd.desc.replace(/[+]/g," ") + "</p>";
  var divEnd   = "</div>";

  $('div#cards').append(divStart + h1Line + pLine + descLine + divEnd);
}

function resetForm(){
  $('form .finput').val('');
  $('#first').focus();
}

$(document).ready(function(){
  $('form').submit(function(){
    var temp;
    var fdata = {};
    var fdSerial = $(this).serialize().split('&');
    for (var i = 0; i < fdSerial.length; i++){
      temp = fdSerial[i].split('=');
      if (temp[1] !== ""){
        fdata[temp[0]] = temp[1];
      } else {
        switch (temp[0]){
          case "fn":
            alert("First Name can't be empty");
            break;
          case "ln":
            alert("Last Name can't be empty");
            break;
          case "desc":
            alert("Description can't be empty");
            break;
        }
        return false;
      }
    }
    resetForm();
    putCard(fdata);
    return false;
  })

  $('div#cards').on("click","div",function(){
    $(this).animate({width:"0"},{queue: false, duration: 1000});
    $(this).animate({fontSize:"0"},1000);
    $(this).promise().done(function(){
      if ($(this).children('.desc').css('display') === "none"){    
        $(this).children('h1').hide()
        $(this).children('p').hide();
        $(this).children('.desc').show();
      } else {
        $(this).children('h1').show()
        $(this).children('p').show();
        $(this).children('.desc').hide();        
      }
    })
    $(this).promise().done(function(){
      $(this).animate({width:"90%"}, {queue: false, duration: 1000});
      $(this).animate({fontSize:"25px"},1000);
    })
  })
})
