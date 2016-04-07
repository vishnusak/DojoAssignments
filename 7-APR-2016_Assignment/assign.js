/// Construct a function to accept four parameters. Print all multiples of param1 from param2 to param3 inclusive unless multiple is equal to param4. Use a WHILE loop. Given (3,5,17,9), print 6,12,15 (which are all of the multiples of 3 between 5 and 17, except for 9).
function q1(num, ll, ul, ex){
  if ((ll < num) && (ul < num)){
    console.log("The Lower and Upper limits of the range have to be greater than Number");
  } else if (ll > ul){
    for (var i = ll; i >= ul; i--){
      if (((i % num) === 0) && (i !== ex)){
        console.log(i);
      }
    }
  } else if (ul >= ll){
    for (var i = ll; i <= ul; i++){
      if (((i % num) === 0) && (i !== ex)){
        console.log(i);
      }
    }
  }
}

//// Build a function that accepts two numbers. If they represent the month and day you were born – in either order – log "How did you know?" Otherwise, log "Just another day...."
function q2(num1, num2){
  if (num1 === 3){
    if (num2 === 6){
      console.log("How did you know?!");
    } else {
      console.log("Just another day....");
    }
  } else if (num1 === 6){
    if (num2 === 3){
      console.log("How did you know?!");
    } else {
      console.log("Just another day....");
    }
  } else {
    console.log("Just another day....");
  }
}

// Create a function that accepts a number as an input. Return an array that counts down by one, from the number (as array’s ‘zero’th element) down to 0 (as the last element). How long is this array?
function q3arr(num){
  var arr = [];
  for (var i = num; i >= 0; i--){
    arr.push(i);
  }
  return arr;
}

function q3(){
  var i = 10;
  var ret = q3arr(i);

  console.log(ret);
  console.log(ret.length);
}

// Your function will receive an array with two numbers. Print the first value, and return the second.
function q4pnr(num_arr){
  console.log(num_arr[0]);
  return num_arr[1];
}

function q4(){
  var i = [85, 67];
  var ret = q4pnr(i);
  console.log(ret);
}

// Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).
function q5arrsum(arr){
  return arr[0] + arr.length;
}

function q5(){
  var i = [1,2,3,4,5,6,7,8,9];
  var ret = q5arrsum(i);
  console.log(ret);
}

//Q6 and Q7 repeated from the assignment on 5th Apr (W1D1)

// For array [1,3,5,7,9,13], print the numbers that are greater than its 2nd value. Return how many values this is.
function q6greater(numArr){
  var secEle = numArr[1];
  var result = [];
  for (var i = 0; i < numArr.length; i++){
    if (numArr[i] > secEle) {
      result.push(numArr[i]);
    }
  }
  console.log(result);
  return result.length;
}

function q6(){
  var i = [1,3,5,7,9,13];
  var ret = q6greater(i);
  console.log(ret);
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
  var i = [];
  var iSize = Math.floor(Math.random() * 10) + 1;
  var ret = [];

  for (var x = 0; x <= iSize; x++){
    i.push(Math.floor(Math.random() * 100));
  }

  console.log("Input: Array = [" + i + "]  Length = " + i.length);
  ret = q7retGreat(i);
  console.log(ret.length);
}

// Build a function that takes two numbers num1 and num2. It should return an array of length num1, where each value is num2. Print "Jinx!" if the numbers are the same.
function q8jinx(num1, num2){
  var arr = [];
  if (num1 === num2){
    console.log("Jinx!");
  }

  for (var i = 0; i < num1; i++){
    arr.push(num2);
  }
  return arr;
}

function q8(){
  var x = 4;
  var y = 2;
  var ret = q8jinx(x,y);
  console.log(ret);
}