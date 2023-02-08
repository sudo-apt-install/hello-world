// FUNCTION DEFINITION(S)
function map(array, callbackFunction) {
  var newArray = [];

  for (var i = 0; i < array.length; i++) {
    let element = array[i];
    
    //apply CB function then store result in newArray
    let result = callbackFunction(element);
    newArray.push(result);
  }

  return newArray;
}

function cubeAll(numbers) {
  return map(numbers, function(n) {
    return n ** 3;
  });
}

// ASSERTION FUNCTION(S) TO BE USED

function assertArraysEqual(actual, expected, testName){
  let hasSameValues = true;
  for (var i = 0; i < actual.length; i++){
    if (actual[i] !== expected[i]) {
      hasSameValues = false;
      break;
    }
  }
  
  let hasSameLengths = actual.length === expected.length;
  
  if (hasSameValues && hasSameLengths) {
    console.log ('passed');
  }else{
    console.log ('FAILED [' + testName + '] Expected "' + expected + '" but got ' + actual);
  }
}

// TESTS SUITE
function addOne(val){
  return val + 1;
}

var inputForMap = [1, 2, 3]
var actualMap = map(inputForMap, addOne);
var expectedMap = [2, 3, 4];
assertArraysEqual(actualMap, expectedMap, "Should correctly map elements of an array");

var inputForCubeAll = [1, 3, 5];
var actualCubeAll = cubeAll(inputForCubeAll);
var expectedCubeAll = [1, 27, 125];
assertArraysEqual(actualCubeAll, expectedCubeAll, "Should correctly cube all elements of an array");
