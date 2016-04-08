function closeAll(){
  var sol = document.getElementsByClassName('soln');

  for(var i=0; i< sol.length; i++){
    sol[i].style.display = "";
  }
}

function oc(q){
  var qq = document.getElementById(q);
  if (qq.style.display == ""){
    closeAll();
    qq.style.display = "block";
    switch (q){
      case 'q1':
        document.getElementById('pq1').innerHTML = "";
        break;
      case 'q2':
        document.getElementById('pq2').innerHTML = "";
        break;
      case 'q3':
        document.getElementById('pq3').innerHTML = "";
        break;
      case 'q4':
        document.getElementById('pq4').innerHTML = "";
        break;
      case 'q5':
        document.getElementById('pq5').innerHTML = "";
        break;
      case 'q6':
        document.getElementById('pq6').innerHTML = "";
        q6();
        break;
      case 'q7':
        document.getElementById('pq7').innerHTML = "";
        break;
      case 'q8':
        document.getElementById('pq8').innerHTML = "";
        break;
    }
  } else {
    qq.style.display = "";
  }
}

/// Construct a function to accept four parameters. Print all multiples of param1 from param2 to param3 inclusive unless multiple is equal to param4. Use a WHILE loop. Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, except for 9).
function q1(){
  if (document.getElementById('q1b').innerHTML == "Clear"){
    document.getElementById('pq1').innerHTML = "";
    document.getElementById('num').value = "";
    document.getElementById('ll').value = "";
    document.getElementById('ul').value = "";
    document.getElementById('ex').value = "";
    document.getElementById('q1b').innerHTML = "Print";
    document.getElementById('num').focus();
    return;
  }

  document.getElementById('pq1').innerHTML = "";
  var num = parseInt(document.getElementById('num').value);
  var ll  = parseInt(document.getElementById('ll').value);
  var ul  = parseInt(document.getElementById('ul').value);
  var ex  = parseInt(document.getElementById('ex').value);

  if (isNaN(num) || isNaN(ll) || isNaN(ul) || isNaN(ex)){
    document.getElementById('pq1').innerHTML = "Please provide valid numbers for all 4 inputs.";
    document.getElementById('num').focus();
  } else {
    document.getElementById('q1b').innerHTML = "Clear";
    if ((ll < num) && (ul < num)){
      document.getElementById('pq1').innerHTML = "The range (Lower and Upper) has to be greater than Number.";
    } else if (ll > ul){
      for (var i = ll; i >= ul; i--){
        if (((i % num) === 0) && (i !== ex)){
          document.getElementById('pq1').innerHTML += i + ' ; ';
        }
      }
    } else if (ul >= ll){
      for (var i = ll; i <= ul; i++){
        if (((i % num) === 0) && (i !== ex)){
          document.getElementById('pq1').innerHTML += i + ' ; ';
        }
      }
    }
  }
}

//// Build a function that accepts two numbers. If they represent the month and day you were born – in either order – log "How did you know?" Otherwise, log "Just another day...."
function q2(){
  if (document.getElementById('q2b').innerHTML == "Clear"){
    document.getElementById('pq2').innerHTML = "";
    document.getElementById('num1').value = "";
    document.getElementById('num2').value = "";
    document.getElementById('q2b').innerHTML = "Check";
    document.getElementById('num1').focus();
    return;
  }

  document.getElementById('pq2').innerHTML = "";
  var num1 = parseInt(document.getElementById('num1').value);
  var num2 = parseInt(document.getElementById('num2').value);

  if (isNaN(num1) || isNaN(num2)){
    document.getElementById('pq2').innerHTML = "Please provide valid numbers for both inputs.";
    document.getElementById('num1').focus();
  } else {
    document.getElementById('q2b').innerHTML = "Clear";
    if (num1 === 3){
      if (num2 === 6){
        document.getElementById('pq2').innerHTML = "How did you know?!";
      } else {
        document.getElementById('pq2').innerHTML = "Just another day....";
      }
    } else if (num1 === 6){
      if (num2 === 3){
        document.getElementById('pq2').innerHTML = "How did you know?!";
      } else {
        document.getElementById('pq2').innerHTML = "Just another day....";
      }
    } else {
      document.getElementById('pq2').innerHTML = "Just another day....";
    }
  }
}

// Create a function that accepts a number as an input. Return an array that counts down by one, from the number (as array’s ‘zero’th element) down to 0 (as the last element). How long is this array?
function q3(){
  if (document.getElementById('q3b').innerHTML == "Clear"){
    document.getElementById('pq3').innerHTML = "";
    document.getElementById('num3').value = "";
    document.getElementById('q3b').innerHTML = "See Array";
    document.getElementById('num3').focus();
    return;
  }

  document.getElementById('pq3').innerHTML = "";
  var num = parseInt(document.getElementById('num3').value);
  var arr = [];

  if (isNaN(num)){
    document.getElementById('pq3').innerHTML = "Please provide a valid number input";
    document.getElementById('num3').focus();
  } else {
    document.getElementById('q3b').innerHTML = "Clear";
    for (var i = num; i >= 0; i--){
      arr.push(i);
      document.getElementById('pq3').innerHTML += i + ' ; ';
    }
    document.getElementById('pq3').innerHTML += "<br /><br />The length of this array is " + arr.length;
  }
}

// Your function will receive an array with two numbers. Print the first value, and return the second.
function q4(){
  if (document.getElementById('q4b').innerHTML == "Clear"){
    document.getElementById('pq4').innerHTML = "";
    document.getElementById('num41').value = "";
    document.getElementById('num42').value = "";
    document.getElementById('q4b').innerHTML = "Print";
    document.getElementById('num41').focus();
    return;
  }

  document.getElementById('pq4').innerHTML = "";
  var num_arr = [];
  num_arr[0] = parseInt(document.getElementById('num41').value);
  num_arr[1] = parseInt(document.getElementById('num42').value);

  if (isNaN(num_arr[0]) || isNaN(num_arr[1])){
    document.getElementById('pq4').innerHTML = "Please provide an array with 2 numbers";
    document.getElementById('num41').focus();
  } else {
    document.getElementById('q4b').innerHTML = "Clear";
    document.getElementById('pq4').innerHTML = "The first element of the input array is " + num_arr[0];
    document.getElementById('pq4').innerHTML += "<br /><br />The second element of the input array is " + num_arr[1];
  }
}

// Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

function q5(num){
  document.getElementById('pq5').innerHTML = "";
  switch (num){
    case 1:
      var i = [1,2,3,4,5];
      document.getElementById('pq5').innerHTML = "For Numeric Array input:";
      document.getElementById('pq5').innerHTML += "<br /><br />Input Array: [1,2,3,4,5]";
      document.getElementById('pq5').innerHTML += "<br /><br />Output: First Element = " + i[0] +' ; ';
      document.getElementById('pq5').innerHTML += "Length = " + i.length + " ; ";
      document.getElementById('pq5').innerHTML += "Sum = " + (i.length + i[0]);
      break;
    case 2:
      var j = ["String",2,3,4,5];
      document.getElementById('pq5').innerHTML = "For Array input with a STRING:";
      document.getElementById('pq5').innerHTML += "<br /><br />Input Array: ['String',2,3,4,5]";
      document.getElementById('pq5').innerHTML += "<br /><br />Output: First Element = " + j[0] +' ; ';
      document.getElementById('pq5').innerHTML += "Length = " + j.length + " ; ";
      document.getElementById('pq5').innerHTML += "Sum = " + (j.length + j[0]);
      break;
    case 3:
      var k = [false,2,3,4,5];
      document.getElementById('pq5').innerHTML = "For Array input with a BOOLEAN:";
      document.getElementById('pq5').innerHTML += "<br /><br />Input Array: [false,2,3,4,5]";
      document.getElementById('pq5').innerHTML += "<br /><br />Output: First Element = " + k[0] +' ; ';
      document.getElementById('pq5').innerHTML += "Length = " + k.length + " ; ";
      document.getElementById('pq5').innerHTML += "Sum = " + (k.length + k[0]);
      break;
  }
}

//Q6 and Q7 repeated from the assignment on 5th Apr (W1D1)

// For array [1,3,5,7,9,13], print the numbers that are greater than its 2nd value. Return how many values this is.
function q6(){
  var arr = [1,3,5,7,9,13];
  var secEle = arr[1];
  var result = [];
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > secEle) {
      result.push(arr[i]);
    }
  }
  document.getElementById('pq6').innerHTML = "Input Array: " + arr;
  document.getElementById('pq6').innerHTML += "<br /><br />Result: " + result;
  document.getElementById('pq6').innerHTML += "<br /><br />Result Length: " + result.length;
}

// Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?
function q7retGreat(inArr){
  var secEle;
  var result    = [];

  if (inArr.length > 1){
    secEle = inArr[1];

    for (var i = 0; i < inArr.length; i++){
      if (inArr[i] > secEle) {
        result.push(inArr[i]);
      }
    }
  }
  return result;
}

function q7(){
  if (document.getElementById('q7b').innerHTML == "Clear"){
    document.getElementById('pq7').innerHTML = "";
    document.getElementById('q7b').innerHTML = "Try it";
    return;
  }

  document.getElementById('pq7').innerHTML = "";
  document.getElementById('q7b').innerHTML = "Clear"

  var i = [];
  var iSize = Math.floor(Math.random() * 10) + 1;
  var ret = [];

  for (var x = 0; x <= iSize; x++){
    i.push(Math.floor(Math.random() * 100));
  }

  document.getElementById('pq7').innerHTML += "Input array = [" + i + "];<br /><br />Length = " + i.length;
  if (i.length > 1){
    ret = q7retGreat(i);
    document.getElementById('pq7').innerHTML += "<br /><br />The second element = " + i[1];
    document.getElementById('pq7').innerHTML += "<br /><br />There are " + ret.length + " element(s) greater.";
    document.getElementById('pq7').innerHTML += "<br /><br />They are = [" + ret + "]";
  } else {
    document.getElementById('pq7').innerHTML += "<br /><br />Only 1 element. Clear and Try again";
  }
}

// Build a function that takes two numbers num1 and num2. It should return an array of length num1, where each value is num2. Print "Jinx!" if the numbers are the same.
function q8jinx(num1, num2){
  var arr = [];
  if (num1 === num2){
    document.getElementById('pq8').innerHTML = "Jinx!<br /><br />";
  }

  for (var i = 0; i < num1; i++){
    arr.push(num2);
  }
  return arr;
}

function q8(){
  if (document.getElementById('q8b').innerHTML == "Clear"){
    document.getElementById('pq8').innerHTML = "";
    document.getElementById('num81').value = "";
    document.getElementById('num82').value = "";
    document.getElementById('q8b').innerHTML = "Print";
    document.getElementById('num81').focus();
    return;
  }

  document.getElementById('pq8').innerHTML = "";
  var x = parseInt(document.getElementById('num81').value);
  var y = parseInt(document.getElementById('num82').value);

  if (isNaN(x) || isNaN(y)){
    document.getElementById('pq8').innerHTML = "Please provide valid number inputs";
    document.getElementById('num81').focus();
  } else {
    document.getElementById('q8b').innerHTML = "Clear";
    var ret = q8jinx(x,y);
    document.getElementById('pq8').innerHTML += "The array is: [" + ret + "]";
    document.getElementById('pq8').innerHTML += "<br /><br />The length is: " + ret.length;
  }
}
