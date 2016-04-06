// 1.  Set variable myNumber equal to the value 42. Then set
// variable myName equal to your name. Now swap values – put
// the value of myNumber into myName, and vice versa.
function swap(){
  var numTB   = document.getElementById("swap1");
  var nameTB  = document.getElementById("swap2");
  var oNumTB  = document.getElementById("swap3");
  var oNameTB = document.getElementById("swap4");

  var myNumber = numTB.value;
  var myName   = nameTB.value;
  var temp;

  temp     = myNumber;
  myNumber = myName;
  myName   = temp;

  oNumTB.value          = myNumber;
  oNameTB.value         = myName;
  // document.getElementById("pswap").innerHTML = "Output After Swapping";
  // document.getElementById("pswap").style.display  = 'block';
  // document.getElementById("lswap3").style.display = 'inline';
  // document.getElementById("lswap4").style.display = 'inline';
}

// 2.  Create a function named beCheerful(). Within this function, 
// console.log “good morning!” Call this function 84 times.
function beCheerful(){
  for (var i = 1; i <= 84; i++) {
    console.log(i + "-good morning");
  }
  document.getElementById("pq2out").innerHTML = "Check the Console Log for 84 'good morning's";
}

// 3. Print all integers from -52 to 1066, with FOR loop.
function printInt(){
  var numArr = [];
  for (var i = -52; i <= 1066; i++) {
    numArr.push(i);
  }

  document.getElementById("pq3out").innerHTML = numArr;  
}

// 4. For [1,3,5,7,9,13], print values that are greater than 2nd value.
function printGreater(){
  var numArr = [1,3,5,7,9,13];
  var secEle = numArr[1];
  var result = [];
  for (var i = 0; i < numArr.length; i++){
    if (numArr[i] > secEle) {
      result.push(numArr[i]);
    }
  }

  document.getElementById("pq4out").innerHTML = result;
}

// 5. Given an array, return a new array with just
// values that are greater than the array’s second value (arr[1]).
// Pay attention to the input. What if the array is too short?
function returnGreater(){
  var inArr     = [];
  var inArrSize = Math.floor(Math.random() * 10) + 1;
  var secEle;
  var result    = [];

  for (var i = 0; i <= inArrSize; i++){
    inArr.push(Math.floor(Math.random() * 100));
  }

  document.getElementById("pq5in").innerHTML = "Input: Array = [" + inArr + "]  Length = " + inArr.length;

  if (inArr.length > 1){
    secEle = inArr[1];

    for (var i = 0; i < inArr.length; i++){
      if (inArr[i] > secEle) {
        result.push(inArr[i]);
      }
    }

    if (result.length == 0){
      document.getElementById("pq5out").innerHTML = "Output: Second Element = " + secEle + " Result Array is Empty since second element is the largest in the array";
    } else {
      document.getElementById("pq5out").innerHTML = "Output: Second Element = " + secEle + " Result Array = [" + result + "]";      
    }
  } else {
    document.getElementById("pq5out").innerHTML   = "Output: Input Array is not long enough";
  }
}

// 6. Print integers 2000-5280 inclusive, with WHILE.
function whilePrint(){
  var i      = 2000;
  var numArr = [];

  while (i <= 5280) {
    numArr.push(i);
    i++;
  }
  document.getElementById("pq6out").innerHTML = numArr;
}

// 7. Print all multiples of 3 from 6 to 60,000. Do this using a WHILE loop.
function multiple(){
  var i      = 1;
  var numArr = [];

  while ((i*3) <= 60000){
    numArr.push(i*3);
    i++;
  }
  document.getElementById("pq7out").innerHTML = numArr;
}