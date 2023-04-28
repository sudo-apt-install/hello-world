// FUNCTION DEFINITION(S)
function findMaxRepeatCountInWord(word) {
  // Break up individual word into individual letters.
  var letters = word.split("");
  var letterContainer = {};
  // Count the instances of each letter
  // Iterate all the counts and find the highest
  
  for (var i = 0; i < letters.length; i++) {
    var currentLetter = letters[i].toLowerCase();
    if (letterContainer[currentLetter] === undefined){
      letterContainer[currentLetter] = 1;
    } else{
      letterContainer[currentLetter]++;
    }
  }
  // Return this word's max repeat count
  
  var maxCount = 0;
  
  for (letter in letterContainer){
    if (letterContainer[letter] > maxCount){
      maxCount = letterContainer[letter];
    }
  }
  
  return maxCount;
}

function findFirstWordWithMostRepeatedChars(text) {
  var maxRepeatCountOverall = 0;
  var wordWithMaxRepeatCount = '';

  // Break up input text into words (space-delimited).
  var words = text.split(" ");
  // For each word...
  for (var j = 0; j < words.length; j++) {
    var word = words[j];
    var repeatCountForWord = findMaxRepeatCountInWord(word)
    
    // If that max repeat count is higher than the overall max repeat count, then
    if (repeatCountForWord > maxRepeatCountOverall){
      // update maxRepeatCountOverall
      maxRepeatCountOverall = repeatCountForWord;
      
      // update wordWithMaxRepeatCount
      wordWithMaxRepeatCount = word;
    }
  }

  return wordWithMaxRepeatCount;
}

// ASSERTION FUNCTION(S) TO BE USED

function assertCount(actual, expected, testName){
  if (actual === expected) {
    console.log('passed');
  }else{
    console.log ('FAILED [' + testName + '] expected "' + expected + '" but got "' + actual + '" ');
  }
}

// TESTS CASES

var input1 = "supercalifragilisticexpialidocious";
var actualInput = findMaxRepeatCountInWord(input1);
var expected1 = 7;
assertCount(actualInput, expected1, "");


var input2 = "I make these sacrifices for you are you not entertained"
var actual2 = findFirstWordWithMostRepeatedChars(input2);
var expected2 = "entertained";
assertCount(actual2, expected2, "should return the word with the most repeated characters")
