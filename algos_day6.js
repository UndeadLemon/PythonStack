// /* 
//   Given an array of strings
//   return the number of times each string occurs (a frequency / hash table)
// */

// // const arr1 = ["a", "a", "a"];
// // const expected1 = {
// //   a: 3,
// // };

// // const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
// // const expected2 = {
// //   a: 2,
// //   b: 1,
// //   c: 3,
// //   B: 1,
// //   d: 1,
// // };

// // const arr3 = [];
// // const expected3 = {};

// /**
//  * Builds a frequency table based on the given array.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {Array<string>} arr
//  * @returns {Object<string, number>} A frequency table where the keys are items
//  *    from the given arr and the values are the amnt of times that item occurs.
//  */

// // function makeFrequencyTable(arr) {
// //     let newObj = {}
// //     for(let i = 0; i<arr.length;i++){
// //         if(!(arr[i] in newObj)){
// //             newObj[arr[i]]=1
// //         }
// //         else{
// //             newObj[arr[i]]++
// //         }
// //     }
// //     return newObj
// // }

// // console.log(makeFrequencyTable(arr2))

// /* 
// Given a non-empty array of odd length containing ints where every int but one
// has a matching pair (another int that is the same)
// return the only int that has no matching pair.
// */

// const nums1 = [1];
// const expected1 = 1;

// const nums2 = [5, 4, 5];
// const expected2 = 4;

// const nums3 = [5, 4, 3, 4, 3, 4, 5];
// const expected3 = 4; // there is a pair of 4s but one 4 has no pair.

// const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
// const expected4 = 1;

// function oddOccurrencesInArray(arr) {

//     let results = []
//     let newObj = {}
//     for(let i = 0; i<arr.length;i++){
//         if(!(arr[i] in newObj)){
//             newObj[arr[i]]=1
//         }
//         else{
//             newObj[arr[i]]++
//         }
//     }
//     for (key in newObj){
//         if(!(newObj[key]%2===0)){
//             results.push(key)
//         }
//     }
//     if (results.length === 1){
//         return results[0]
//     }

//     return results
// }

// console.log(oddOccurrencesInArray(nums1))

console.log("test 1")

function toCamelCase(str) {
    console.log("test 2")
    let newStr = ""
    for (let i = 0; i < str.length; i++) {
        console.log(i)
        if (i = 0) {
            console.log(str[i])
            newStr.push(str[i])
        }
        else if (str[i] == str[i].toUpperCase() && str[i] != str[i].toLowerCase()) {
            newStr.push(str[i].toLowerCase())
        }
    
    }
    return newStr
}

console.log(toCamelCase("the_STealth_Warrior"))