const str = "Hello World";

const rotateAmnt1 = -5;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 123172613261235;
const expected5 = "ldHello Wor";

const rotateAmnt6 = 11;
const expected6 = "Hello World";


function rotateStr(str,amnt){
    if(amnt === str.length || str.length%amnt===0 || amnt === 0){
        return str
    }
    // while(amnt > str.length){
    //     amnt = amnt - str.length
    // }
    amnt = amnt%str.length
    newStr=""
    for(let i = str.length-amnt;i < str.length;i++){
    newStr += str[i]

    }
    newStrAdd=""
    for(let i = 0;i<str.length-amnt;i++){
        newStrAdd += str[i]
    }

    newStr += newStrAdd
    return newStr
}
    // let arr = []
    // arr = str.split("")
    // let newArr = arr.slice(-amnt)
    // arr = arr.slice(0,str.length - amnt)
    // newStr = newArr.join("")
    // arr = arr.join("")
    // newStr += arr

    // newStr = newArr.join("")
    // testStr = str.slice(-amnt)
    // testStr +=
    // newStr += str


console.log(rotateStr(str, rotateAmnt1))

/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

// const strA1 = "ABCD";
// const strB1 = "CDAB";
// // Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated
// const expected1 = true;

// const strA2 = "ABCD";
// const strB2 = "CDBA";
// // Explanation: all same letters in 2nd string, but out of order
// const expected2 = false;

// const strA3 = "ABCD";
// const strB3 = "BCDAB";
// // Explanation: same letters in correct order but there is an extra letter.
// const expected3 = false;

// /**
//  * Determines whether the second string is a rotated version of the first.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} s1
//  * @param {string} s2
//  * @returns {boolean} Whether the second string is a rotated version of the 1st.
//  */
// function isRotation(s1, s2) {
//     if(s2.length != s1.length){
//         return false
//     }
//     s2 += s2
//     return s2.includes(s1)

// }

// console.log(isRotation(strA1,strB1))