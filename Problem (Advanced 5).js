//Write a function called "sumDigits".
//
//Given a number, "sumDigits" returns the sum of all its digits.

//var output = sumDigits(1148);
//console.log(output); // --> 14
//
//If the number is negative, the first digit should count as negative.
//
//var output = sumDigits(-316);
//console.log(output); // --> 4



function sumDigits(num) {
  
  var numToString = num.toString(); 
  var seperatedDigits = numToString.split('');
  
  if (seperatedDigits[0] === "-"){
    seperatedDigits[1] = seperatedDigits[1] * -1;
    seperatedDigits.splice(0, 1);
  }
  
  var counter = Number(0);
  
  for (var i = 0; i < seperatedDigits.length; i++) {
    counter += Number(seperatedDigits[i]);
  }
  
  return counter;
  
}

// Test cases

var output = sumDigits(1148);
console.log(output); // --> 14

var output = sumDigits(-316);
console.log(output); // --> 4