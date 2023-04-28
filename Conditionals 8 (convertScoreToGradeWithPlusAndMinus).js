/*

Write a function called "convertScoreToGradeWithPlusAndMinus".

Given a score, "convertScoreToGradeWithPlusAndMinus" returns a string representing the letter grade corresponding to the given score.

Notes:

    (100 - 90) --> 'A'
    (89 - 80) --> 'B'
    (79 - 70) --> 'C'
    (69 - 60) --> 'D'
    (59 - 0) --> 'F'
    If the given score is greater than 100 or less than 0, it should return 'INVALID SCORE'.
    If the score is between the 0 and 2 (inclusive) of a given range, return the letter with a '-'
    If the score is between the 8 and 9 (inclusive) of a given range, return the letter with a '+'
    There are is no F+ and there is no F-.

*/

function convertScoreToGradeWithPlusAndMinus(score) {
  
  if (score > 100 || score < 0) {
    return "INVALID SCORE"
  }
  
  var lastDigitStr = String(score).slice(-1);
  var lastDigitNum = Number(lastDigitStr);
  var plus = '+';
  var minus = '-';
  
  var grade = '';
  var letterGrades = ['A', 'B', 'C', 'D', 'F'];
  
  if (score >= 90){
    grade = letterGrades[0];
  } else if (score >= 80 && score < 90){
    grade = letterGrades[1];
  } else if (score >= 70 && score < 80){
    grade = letterGrades[2];
  } else if (score >= 60 && score < 70){
    grade = letterGrades[3];
  } else if (score >= 0 && score < 60){
    grade = letterGrades[4];
  }
  
  if (lastDigitNum >= 0 && lastDigitNum <= 2 && score > 59 && score != 100){
    grade = grade.concat(minus);
  } else if (lastDigitNum >= 8 && lastDigitNum <= 9 && score > 59 && score != 100){
    grade = grade.concat(plus);
  } else if (score === 100){
    grade = grade.concat(plus);
  }
  
  return grade;
}

//Test case
var output = convertScoreToGradeWithPlusAndMinus(91);
console.log(output); // --> 'A-'