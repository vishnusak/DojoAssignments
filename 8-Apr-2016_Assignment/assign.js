function  start(){
  var sbtn = document.getElementById('start');
  var page = document.getElementById('page');
  var arr = [];

  for (var i = 1; i<= 6; i++){
    arr.push(document.getElementById('q'+i));
  }

  qarr = arr; //Global Variable

  sbtn.style.display = 'none';
  page.style.display = 'block';
  qarr[0].classList.add('qstart');
  qarr[0].style.display = 'block';
}

function pg(dir){
  var gotit = 0;
  var i = 0;
  
  while (gotit === 0){
    if (qarr[i].style.display === 'block'){
      gotit = 1;
    } else {
      i++;
    }
  }

  qarr[i].classList.remove('qstart');
  qarr[i].classList.add('qend');
  qarr[i].style.display = 'none';

  switch(dir){
    case -1:
      if (i === 0){
        qarr[5].classList.remove('qend');
        qarr[5].classList.add('qstart');
        qarr[5].style.display = 'block';
        qarr[5].getElementsByTagName('P')[0].innerHTML = '';
        if (qarr[5].getElementsByTagName('input').length > 0){
          for (var x = 0;x < qarr[5].getElementsByTagName('input').length;x++){
            qarr[5].getElementsByTagName('input')[x].value = '';
          }
        }
      } else {
        qarr[i-1].classList.remove('qend');
        qarr[i-1].classList.add('qstart');
        qarr[i-1].style.display = 'block';
        qarr[i-1].getElementsByTagName('P')[0].innerHTML = '';
        if (qarr[i-1].getElementsByTagName('input').length > 0){
          for (var x = 0;x < qarr[i-1].getElementsByTagName('input').length;x++){
            qarr[i-1].getElementsByTagName('input')[x].value = '';
          }
        }
      }
      break;
    case 1:
      if (i === 5){
        qarr[0].classList.remove('qend');
        qarr[0].classList.add('qstart');
        qarr[0].style.display = 'block';
        qarr[0].getElementsByTagName('P')[0].innerHTML = '';
        if (qarr[i-1].getElementsByTagName('input').length > 0){
          for (var x = 0;x < qarr[i-1].getElementsByTagName('input').length;x++){
            qarr[i-1].getElementsByTagName('input')[x].value = '';
          }
        }
      } else {
        qarr[i+1].classList.remove('qend');
        qarr[i+1].classList.add('qstart');
        qarr[i+1].style.display = 'block';
        qarr[i+1].getElementsByTagName('P')[0].innerHTML = '';
        if (qarr[i+1].getElementsByTagName('input').length > 0){
          for (var x = 0;x < qarr[i+1].getElementsByTagName('input').length;x++){
            qarr[i+1].getElementsByTagName('input')[x].value = '';
          }
        }
      }
      break;
  }
}

// Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!"; if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".
function q1(){
  if (document.getElementById('q1b').innerHTML === 'Clear'){
    document.getElementById('pq1').innerHTML = '';
    document.getElementById('q1b').innerHTML = 'Fit It';
    for (var i = 0; i <= 9; i++){
      document.getElementById('q1'+i).value = '';
    }
    document.getElementById('q10').focus();
    return;
  }

  var arr = [];
  var j   = 0;

  document.getElementById('pq1').innerHTML = '';
  document.getElementById('q1b').innerHTML = 'Clear';
  
  for (var i = 0; i <= 9; i++){
    if(!isNaN(parseInt(document.getElementById('q1'+i).value))){
      arr[j] = parseInt(document.getElementById('q1'+i).value);
      j++;
    }
  }

  if (arr.length > 1){
    var out = (arr[0] == arr.length) ? "Just right!" : ((arr[0] < arr.length) ? "Too small!" : "Too Big!");
    document.getElementById('pq1').innerHTML = "First Element: " + arr[0] + "<br /><br />Array Length: " + arr.length + "<br /><br />" +out;
  } else {
    document.getElementById('pq1').innerHTML = "Please enter some numbers to try this out";
  }
}

//// Fahrenheit To Celsius
// Create a function named fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit, and returns the equivalent temperature as expressed in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.

// Doing it in single line. Not ideal for readability.
function fahrenheitToCelsius(fDegrees){
  if (!isNaN(fDegrees)){
    return (((fDegrees - 32) * 5)/9);
  } else {
    return NaN;
  }
}

function q2(){
  if (document.getElementById('q2b').innerHTML === 'Clear'){
    document.getElementById('pq2').innerHTML = '';
    document.getElementById('q2b').innerHTML = 'Convert It';
    document.getElementById('q20').value = '';
    document.getElementById('q20').focus();
    return;
  }

  document.getElementById('pq2').innerHTML = '';

  var fDegrees = parseInt(document.getElementById('q20').value);
  if (!isNaN(fDegrees)){
    document.getElementById('pq2').innerHTML = fDegrees + "&#176;F = " + fahrenheitToCelsius(fDegrees) + "&#176;C";
    document.getElementById('q2b').innerHTML = 'Clear';
  } else {
    document.getElementById('pq2').innerHTML = "Please enter a number to convert into celsius";
    document.getElementById('q20').focus();
  }
}

// fahrenheitToCelsius(68); //Uncomment to test

//// Celsius to Fahrenheit
// Create a celsiusToFahrenheit(cDegrees) function that accepts a number of degrees in Celsius, and returns the equivalent temperature as expressed in Fahrenheit degrees.
function celsiusToFahrenheit(cDegrees){
  if (!isNaN(cDegrees)){
    return ((cDegrees * 9/5) + 32);
  } else {
    return NaN;
  }
}

function q3(){
  if (document.getElementById('q3b').innerHTML === 'Clear'){
    document.getElementById('pq3').innerHTML = '';
    document.getElementById('q3b').innerHTML = 'Convert It';
    document.getElementById('q30').value = '';
    document.getElementById('q30').focus();
    return;
  }

  document.getElementById('pq3').innerHTML = '';

  var cDegrees = parseInt(document.getElementById('q30').value);
  if (!isNaN(cDegrees)){
    document.getElementById('pq3').innerHTML = cDegrees + "&#176;C = " + celsiusToFahrenheit(cDegrees) + "&#176;F"
    document.getElementById('q3b').innerHTML = 'Clear';
  } else {
    document.getElementById('pq3').innerHTML = "Please enter a number to convert into fahrenheit";
    document.getElementById('q30').focus();
  }

}

// celsiusToFahrenheit(20); //Uncomment to test

//// Fahrenheit IS Celsius
// Is there an integer that is the same temperature in both Fahrenheit and Calsius scales? Use your two functions above to find this value (if it exists at all!).  

// - The answer is -40. -40 C = -40 F. Tried initially from -1000 to +1000. reduced it to -100 - +100 after finding the answer.
function feqc(){
  var ll = -100;
  var ul = 100;
  var ret = [];
  for (var i = ll; i <= ul; i++){
    if (fahrenheitToCelsius(i) == celsiusToFahrenheit(i)){
      ret.push(i);
    }
  }
  if ((ret.length) > 0){
    document.getElementById('pq4').innerHTML = "The integer(s) that is(are) the same temperature in F and C between " + ll + " & " + ul + " is(are) " + ret + " degree(s)";
  } else {
    document.getElementById('pq4').innerHTML = "There are no integers between " + ll + " & " + ul + " that are the same temperature in F and C.";
  }
}

function q4(){
  if (document.getElementById('q4b').innerHTML === 'Clear'){
    document.getElementById('pq4').innerHTML = '';
    document.getElementById('q4b').innerHTML = 'Find It';
    return;
  }

  document.getElementById('pq4').innerHTML = '';
  document.getElementById('q4b').innerHTML = 'Clear';
  feqc();
}

//// Biggie Size
// Given an array, write a function that changes all positive numbers in the array to “big”. Example: makeItBig([-1,3,5,-5]) returns that same array, changed to [-1,"big","big",-5].
function makeItBig(arr){
  for (var i = 0; i < arr.length; i++){
    if (arr[i] > 0){
      arr[i] = 'big';
    }
  }
  return arr;
}

function q5(){
  if (document.getElementById('q5b').innerHTML === 'Clear'){
    document.getElementById('pq5').innerHTML = '';
    document.getElementById('q5b').innerHTML = 'Biggie It';
    for (var i = 0; i <= 9; i++){
      document.getElementById('q5'+i).value = '';
    }
    document.getElementById('q50').focus();
    return;
  }

  var arr = [];
  var j   = 0;
  var ret = [];

  document.getElementById('pq5').innerHTML = '';
  document.getElementById('q5b').innerHTML = 'Clear';

  for (var i = 0; i <= 9; i++){
    if(!isNaN(parseInt(document.getElementById('q5'+i).value))){
      arr[j] = parseInt(document.getElementById('q5'+i).value);
      j++;
    }
  }
  ret = makeItBig(arr);
  document.getElementById('pq5').innerHTML = "The Biggie Sized array is: [" + ret + "]";
}
// console.log(makeItBig([-1,3,5,-5])); //uncomment to test

//// Print Low, Return High
// Create a function that takes array of numbers. The function should print the lowest value in the array, and return the highest value in the array.
function search(arr){
  var high = arr[0], low = arr[0];
  for (var i = 0; i < arr.length; i++){
    high = (arr[i] > high) ? arr[i] : high;
    low = (arr[i] < low) ? arr[i] : low;
  }
  return [low, high];
}

function q6(){
  if (document.getElementById('q6b').innerHTML === 'Clear'){
    document.getElementById('pq6').innerHTML = '';
    document.getElementById('q6b').innerHTML = 'Print It';
    for (var i = 0; i <= 9; i++){
      document.getElementById('q6'+i).value = '';
    }
    document.getElementById('q60').focus();
    return;
  }

  var arr = [];
  var j   = 0;

  document.getElementById('pq6').innerHTML = '';
  document.getElementById('q6b').innerHTML = 'Clear';

  for (var i = 0; i <= 9; i++){
    if(!isNaN(parseInt(document.getElementById('q6'+i).value))){
      arr[j] = parseInt(document.getElementById('q6'+i).value);
      j++;
    }
  }

  if (arr.length > 1){
    var h = [];
    h = search(arr);
    document.getElementById('pq6').innerHTML = "The highest is: " + h[1];
    document.getElementById('pq6').innerHTML += "<br /><br />The lowest is: " + h[0];
  } else {
    document.getElementById('pq6').innerHTML = "Please enter some numbers to try this out";
  }
}
// console.log("The highest is: " + search([99, 430, 746, 112, 982, 918, 87, 0])); //uncomment to test
