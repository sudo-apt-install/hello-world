function findShortestOfThreeWords(word1, word2, word3) {
  var newArray = [word1, word2, word3];
  
  var shortest = newArray[0];
  
  for (var i = 0; i < newArray.length; i++) {
    if (newArray[i].length < shortest.length) {
      shortest = newArray[i];
    }
  }
  return shortest;
}


var output = findShortestOfThreeWords('af', 'two', 'three');
console.log(output); // --> 'a'