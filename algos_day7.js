


function stringDedupe(str){
    
    let newStr = ""
    for(let i = 0;i<str.length;i++){
        if (!(newStr.includes(str[i]))){
            newStr += (str[i])
        }
    }

    return newStr
}

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

const str5 = "yeeeeees";
const expected5 = "yes";

const str_bonus = "SuperTxT";
const expected_bonus = "SuperxT";

console.log(stringDedupe(str2))

/* 
  Given a string containing space separated words
  Reverse each word in the string.
  If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    newStr=""
    for(let i = 0;i<str.length;i++){
        if(!(str[i] === " ")){
            
        }
    }
}