// function parensValid(str){
//     let stack = []
//     for(let i = 0; i<str.length; i++){
//         if(str[i] === "("){
//             stack.push(0)
//         }
//         if(str[i] === ")"){
//             stack.pop()
//         }


//     }
//     if( stack[0] === 0){}

//     return stack




// }
// console.log("test")
// console.log(parensValid("Th(s(s is) not() a )(( ) (( drill?))))("))

/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {
    let stack = []
    let dict = { "(": ")", "{": "}", "[": "]" }
    for (let i = 0; i < str.length; i++) {
        if (str[i] in dict) { 
            stack.push(str[i]) 
        }
        if (str[i] == dict[stack[stack.length - 1]]) {
            stack.pop(str[i])
        }
    } 
    console.log(stack)
    if(stack.length != 0){
        return false
    }
    else{
        return true
    }

}
console.log(bracesValid(str1))