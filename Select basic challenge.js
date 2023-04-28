function select(arr, obj) {
  //create a result obj
  var result = {};
  
  // iterate over the Array
  for (var i = 0; i < arr.length; i++) {
    //if current key is present in input Object
    if (obj[arr[i]] != undefined) {
      // add input object's property to result object
      result[arr[i]] = obj[arr[i]];
    }
  }
  
  //return the result object
  return result;
  
}


// Test Case

var arr = ['a', 'c', 'e'];
var obj = {
  a: 1,
  b: 2,
  c: 3,
  d: 4
};
var output = select(arr, obj);
console.log(output); // --> { a: 1, c: 3 }