/*

Write a function called "findShortestWordAmongMixedElements".

Given an array, "findShortestWordAmongMixedElements" returns the shortest string within the given array.

Notes:

    If there are ties, it should return the first element to appear in the given array.
    Expect the given array to have values other than strings.
    If the given array is empty, it should return an empty string.
    If the given array contains no strings, it should return an empty string.


*/

function findShortestWordAmongMixedElements(arr) {
  
  var stringElements = [];
  
  for (var i = 0; i < arr.length; i++){
    if (typeof (arr[i]) === 'string'){
      stringElements.push(arr[i]);
    }
  }
  
  if (stringElements.length === 0){
    return "";
  }
  
  var ShortestWord = stringElements[0];
  
  
  for (var i = 0; i < stringElements.length; i++){
    if (stringElements[i].length < ShortestWord.length){
      ShortestWord = stringElements[i];
    }
  }
  
  return ShortestWord;
}

// Test case

var output = findShortestWordAmongMixedElements([4, 'two', 2, 'three']);
console.log(output); // --> 'two'