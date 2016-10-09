$(document).ready(function(){

  $('.message-container').on('click', 'span', function(){
    console.log("comment")
    var cmtBlkId = $(this)[0].id,
        msgId    = cmtBlkId.slice(3)
    $('#cc-' + msgId).slideToggle(500, function(){
      console.log("Slide");
    })
  })

  var clientSocket = io.connect()

  clientSocket.on('new-message', function(formData){
    var msgBlock = createNewMsg(formData)
    $('#msg-container').append(msgBlock)
  })

  clientSocket.on('new-comment', function(formData){
    console.log(formData)
    var cmt = createNewCmt(formData)
    console.log(cmt)
    $('#hr-'+formData.msgId).before(cmt)
  })

  $('#main-msg-form').submit(function(e){
    e.preventDefault()
    if ($('#main-msg-form > textarea').val()){
      var formData = {
        name:    $('#main-msg-form > input[type=hidden]').val(),
        msgText: $('#main-msg-form > textarea').val()
      }
      console.log(formData)
      clientSocket.emit('post-message', formData)
    }
  })

  $('.comment-form').submit(function(e){
    e.preventDefault()
    var cmtMsgId = $(this).attr('id')
    console.log("submitting comment")
    console.log("id: ", cmtMsgId)

    if ($('#'+cmtMsgId+' > textarea').val()){
      console.log($('#'+cmtMsgId+' > textarea').val())
      var cmtData = {
        msgId:   cmtMsgId.slice(4),
        name:    $('#'+cmtMsgId+' > input[type=hidden]').val(),
        cmtText: $('#'+cmtMsgId+' > textarea').val()
      }

      clientSocket.emit('post-comment', cmtData)
    }
  })

})

function createNewMsg(formData){
  var newMsgDiv  = `<div id="${formData.msgId}" class="message">`,
      newMsgUser = `<p>${formData.name}</p>`,
      newMsgTxt  = `<p class="msg-text">${formData.msgText}</p>`,
      newShowCmt = `<span class="show-comment button" id="sc-${formData.msgId}" title="Click to toggle comments"> &#8226;&#32;&#8226;&#32;&#8226; </span>`,
      newCmtDiv  = `<div class="comment-container" id="cc-${formData.msgId}">`,
      newCmtHr   = `<hr class="cmt-div" id="hr-${formData.msgId}">`,
      newCmtForm = `<form class="comment-form" id="${formData.msgId}">` +
                   `<input type="hidden" name="user" value="${formData.name}">`    +
                   `<textarea name="comment" placeholder="${formData.name}: Your comment here"></textarea>` +
                   `<input type="submit" value="Post This" class="button">` +
                   `</form>`,
      closeTags  = `</div> </div> <hr class="msg-div">`

  return newMsgDiv + newMsgUser + newMsgTxt + newShowCmt + newCmtDiv + newCmtHr + newCmtForm + closeTags
}

function createNewCmt(formData){
  var newCmtDiv = `<div class="comment">`,
      newCmtUser= `<p>${formData.name}</p>`,
      newCmtTxt = `<p class="cmt-text">${formData.cmtText}</p>`,
      closeTags = `</div`

  return newCmtDiv + newCmtUser + newCmtTxt + closeTags
}
