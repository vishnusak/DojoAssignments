var EMP = 0;
var GUY = 1;
var RED = 2;
var MIS = 3;
var EXP = 4;

var alive = true;

var toggle = 1;

var     reds = [];
var missiles = [];
var   guypos = {x:0, y:0};
var  guyprev = {x:0, y:0};

var theater = [
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP],
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP],
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP],
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP],
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP],
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP],
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP],
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP,EMP],
                [EMP,EMP,EMP,EMP,EMP,EMP,EMP,GUY,EMP,EMP,EMP,EMP,EMP,EMP,EMP]
              ];


function genRed(){
  var newred = {x:0, y:0};
  var pos = Math.floor(Math.random() * theater[0].length);

  theater[0][pos] = RED;
  newred.y = 0;
  newred.x = pos;

  reds.push(newred);
}

function moveRed(){
  for (var i = 0; i < reds.length; i++){   
    theater[reds[i].y][reds[i].x] = EMP;   // make the current cell of the red empty

    if (reds[i].y < theater.length-1){     // check if the red is at the bottom of the screen. if not, move it down by 1 cell, set it to red 
      reds[i].y++;
      theater[reds[i].y][reds[i].x] = RED;
    } else {
      reds.shift();   // The first will be the one to reach the bottom first so remove it. That way the array size never grows beyond 8 or 9
      i--;            // We are removing an item from the array that is being currently processed (reds), 
                      // so the index has to be adjusted so that the following items get processed properly
    }
  }
}

function drawTheater(){
  // if (!alive){return};

  var scene = '';

  var crash = boom(guypos);
  if (crash){
    theater[guypos.y][guypos.x] = EXP;
    alive = false;
  }

  // if (reds.length > 0){
  //   for (var i = 0; i < reds.length; i++){
  //     if ((guypos.x === reds[i].x) && (guypos.y === reds[i].y)){
  //       theater[guypos.y][guypos.x] = EXP;
  //       reds.splice(i,1);
  //       alive = false;
  //     }
  //   }
  // }

  // if (missiles.length > 0 && reds.length > 0){
  //   for (var i = 0; i < Math.min(missiles.length, reds.length); i++){
  //     if ((missiles[i].x === reds[i].x))
  //   }
  // }

  for (var row = 0; row < theater.length; row++){
    scene += "<div>"
    for (var cell = 0; cell < theater[row].length; cell++){
      switch (theater[row][cell]){
        case 0:
          scene += "<div class='empty'></div>";
          break;
        case 1:
          scene += "<div class='guy'></div>";
          break;
        case 2:
          scene += "<div class='red'></div>";
          break;
        case 3:
          scene += "<div class='missile'></div>";
          break;
        case 4:
          scene += "<div class='explode'></div>";
          break;
      }
    }
    scene += "</div>"
  }
  document.getElementById('theater').innerHTML = scene;
}

drawTheater();

function findGuy(){
  for (var i = 0; i < theater.length; i++){
    for (var j = 0; j < theater[i].length; j++){
      if (theater[i][j] === GUY){
        guypos.x = j;
        guyprev.x = j;
        guypos.y = i;
        guyprev.y = i;
      }
    }
  }
}

findGuy();

function boom(who){
  var target = false;

  for (var i = 0; i < reds.length; i++){
    if (who.x === reds[i].x){
      if (Math.abs(who.y - reds[i].y) <= 0){
        target = true;
        reds.splice(i,1);
      }
    }
  }

  return target;
}

function fireInTheHole(){
  var newMiss = {x:0, y:0};

  if (guypos.y > 0){
    newMiss.x = guypos.x;
    newMiss.y = guypos.y - 1;
  }

  missiles.push(newMiss);
  theater[newMiss.y][newMiss.x] = MIS;
  drawTheater();
}

function missilePath(){
  var redgone;
  for (var i = 0; i < missiles.length; i++){

    theater[missiles[i].y][missiles[i].x] = EMP;
  
    if (missiles[i].y > 0){
      missiles[i].y--;
      redgone = boom(missiles[i]); // ------------------------
      if (!redgone){
        theater[missiles[i].y][missiles[i].x] = MIS;
      } else {
        theater[missiles[i].y][missiles[i].x] = EXP;
        missiles.splice(i,1);
      }
    } else {
      missiles.shift();
      i--;
    }
  }
}

// Move GUY using arrow keys. Fire using space bar
document.onkeydown = onKeyDown;
function onKeyDown(event){
  if (!alive){return}

  guyprev.x = guypos.x;
  guyprev.y = guypos.y;

  switch(event.keyCode){
    case 32:
      fireInTheHole();
      break;
    case 37:
      (guypos.x > 0) ? (guypos.x--) : (guypos.x);
      break;
    case 38:
      (guypos.y > 0) ? (guypos.y--) : (guypos.y);
      break;
    case 39:
      (guypos.x < theater[0].length - 1) ? (guypos.x++) : (guypos.x);
      break;
    case 40:
      (guypos.y < theater.length - 1) ? (guypos.y++) : (guypos.y);
      break;
    default:
      break;
  }

  if (guyprev !== guypos){
    theater[guyprev.y][guyprev.x] = EMP;
    theater[guypos.y][guypos.x] = GUY;
    drawTheater();
  } else {
    console.log("Can't move anymore");
  }
}

function game(){
  if (toggle === 1){
    genRed();
    drawTheater();
    toggle = 0;
  } else {
    moveRed();
    drawTheater();
    toggle = 1;
  }
  missilePath();
  drawTheater();

  if (!alive){
    clearInterval(gameSched); 
    // theater[guypos.y][guypos.x] = EMP;
    // drawTheater();
    return;
  }
}

var gameSched = setInterval(game, 200);