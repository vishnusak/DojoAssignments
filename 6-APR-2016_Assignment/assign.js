//Mouse-over event
function mo(id){
  var q = document.getElementById(id);
  q.style.backgroundColor = "green";
  q.style.color = "white";
}

// Mouse-Out event
function mout(id){
  var q = document.getElementById(id);
  if (q.style.backgroundColor == "green"){
    q.style.backgroundColor = "#AFAFAF";
    q.style.color = "black";
  }
}

//OnClick event
function oc(id){
  document.getElementById(id).style.backgroundColor = "rgb(0,175,0)";  
  document.getElementById(id).style.border = "1px solid green";
  var sol_display = document.getElementsByClassName('soln');
  for (var i = 0; i < sol_display.length; i++){
    sol_display[i].style.visibility = 'hidden';
  }
  switch (id){
    case 'q1':
      document.getElementById('r1').innerHTML = '';
      document.getElementById('1').style.visibility = 'visible';
      q1();
      break;
    case 'q2':
      document.getElementById('r2').innerHTML = '';    
      document.getElementById('2').style.visibility = 'visible';
      q2();
      break;
    case 'q3':
      document.getElementById('r3').innerHTML = '';    
      document.getElementById('3').style.visibility = 'visible';
      q3();
      break;
    case 'q4':
      document.getElementById('r4').innerHTML = '';    
      document.getElementById('4').style.visibility = 'visible';
      q4();
      break;
    case 'q5':
      document.getElementById('incoming').value = '';
      document.getElementById('r5').innerHTML = '';    
      document.getElementById('5').style.visibility = 'visible';
      // q5();
      break;
    case 'q6':
      document.getElementById('first').value = '';    
      document.getElementById('second').value = '';    
      document.getElementById('last').value = '';    
      document.getElementById('r6').innerHTML = '';    
      document.getElementById('6').style.visibility = 'visible';
      // q6();
      break;
    case 'q7':
      document.getElementById('yr').value = '';
      document.getElementById('r7').innerHTML = '';    
      document.getElementById('7').style.visibility = 'visible';
      // q7();
      break;
    case 'q8':
      document.getElementById('r8').innerHTML = '';    
      document.getElementById('8').style.visibility = 'visible';
      q8();
     break;
  }
}

//// 1. Using a FOR loop, print the multiples of 3 from -300 to 0.
// Skip numbers -3 and -6.
function multiples(i){
  console.log(i * 3);
  document.getElementById('r1').innerHTML += (i * 3) + " ; ";
}

function q1(){
  document.getElementById('r1').innerHTML = '';
  for (var i = -100; i <= 0; i++){
    if ((i != -1) && (i != -2)){
      multiples(i);
    }
  }
}

//// 2. Log positive numbers starting at 2016, counting down by fours
// (exclude 0), without a FOR loop.
function positive(i){
  console.log(i);
  document.getElementById('r2').innerHTML += i + " ; ";
}

function q2(){
  document.getElementById('r2').innerHTML = '';
  var i = 2016;
  while (i > 0){
    positive(i);
    i -= 4;
  }
}

//// 3. Print all integer multiples of 5, from 512 to 4096. Afterward,
// also log how many there were.
function print5(i){
  console.log(i * 5);
  document.getElementById('r3').innerHTML += (i * 5) + " ; ";
}

function q3(){
  document.getElementById('r3').innerHTML = '';
  var count = 0;
  for (var i = 1; i < 1000; i++){
    if ((i * 5) > 512){
      print5(i);
      count++;
    }
  }
  console.log(count);
  document.getElementById('r3').innerHTML += "<br /><br />Total Number of integers printed is = " + count;
}

//// 4. Print out all integers from 1 to 100. If the number is evenly
// divisible by 5, print "Coding" instead of the number. If the
// number is evenly divisible by 10, also print " Dojo".
function codingdojo(i){
  console.log(i);
  document.getElementById('r4').innerHTML += i + " ; "
}

function q4(){
  document.getElementById('r4').innerHTML = '';
  for (var i = 1; i <= 100; i++){
    if ((i % 5) == 0){
      if ((i % 10) == 0){
        codingdojo('Coding Dojo');
      } else {
        codingdojo('Coding');
      }
    } else {
      codingdojo(i);
    }
  }
}

//// 5. Your function will be given an input parameter incoming.
// Console.log the value of incoming.
function print(incoming){
  console.log(incoming);
  document.getElementById('r5').innerHTML = incoming;
}

function q5(){
  document.getElementById('r5').innerHTML = '';
  var inc = document.getElementById('incoming').value;
  print(inc);
}

//// 6. Make a function that accepts three parameters: first, second
// and last. Print all the multiples of last, from second to first.
// Do this using a FOR loop.
function print3(i){
  console.log(i);
  document.getElementById('r6').innerHTML += i + ' ; ';
}

function q6(){
  document.getElementById('r6').innerHTML = ''; 
  var first  = document.getElementById('first').value;
  var second = document.getElementById('second').value;
  var last   = document.getElementById('last').value;

  if ((last > first) && (last > second)){
    print3(last + ' is greater than ' + first + ' & ' + second);
    print3("Make sure that 'First' & 'Second' are greater than 'Last'");
  } else {
    if (first > second){
      for (var i = second; i <= first; i++){
        if ((i % last) == 0){
          print3(i);
        }  
      }
    } else {
      for (var i = second; i >= first; i--){
        if ((i % last) == 0){
          print3(i);
        }
      }
    }
  }
}

//// 7. Write a function that determines whether a given year is a leap
// year. If a year is divisible by four, it is a leap year, unless it
// is divisible by 100. However, if it is divisible by 400, then it is.
function leap(i){
  console.log(i);
  document.getElementById('r7').innerHTML = i;
}

function q7(){
  document.getElementById('r7').innerHTML = '';
  var msg1 = " is a Leap Year";
  var msg2 = " is not a Leap Year";
  var year = document.getElementById('yr').value;

  if (year != ''){
    if ((year % 4) == 0){
      if ((year % 100) == 0){
        if ((year % 4) == 0){
          leap(year + msg1);
        } else {
          leap(year + msg2);
        }
      } else {
        leap(year + msg1);
      }
    } else {
      leap(year + msg2);
    }
  } else {
    leap("Please enter the year");
  }
}

//// 8. Print all the odd integers from -300,000 to 300,000.
// What is the sum of all these numbers? (edited)
//****changed the range to -300..300 because the earlier 600000 
//****number range was too taxing for the laptop!
function odd(i){
  console.log(i);
  document.getElementById('r8').innerHTML += i + " ; ";
}

function q8(){
  document.getElementById('r8').innerHTML = '';
  var sum = 0;
  for (var i = -300; i <= 300; i++){
    if ((i % 2) != 0){
      odd(i);
      sum += i;
    }
  }
  console.log(sum);
  document.getElementById('r8').innerHTML += "<br /><br />The sum of all odd integers between -300 and 300 is " + sum;
}