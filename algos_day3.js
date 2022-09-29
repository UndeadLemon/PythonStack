/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

//   const str1 = "aaaabbcddd";
//   const expected1 = "a4b2c1d3";
  
//   const str2 = "";
//   const expected2 = "";
  
//   const str3 = "a";
//   const expected3 = "a";
  
//   const str4 = "bbcc";
//   const expected4 = "bbcc";
  
//   const str5 = "aaaabbcdddaaa";
//   const expected5 = "a7b2c1d3";
//   const expected5_bonus = "a4b2c1d3a3";
  
  
  
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
//   function encodeStr(str) {
//     let result = ""
//     let dict = {}
//     for ( let i = 0; i < str.length; i++){
//         if (str[i] in dict){
//             dict[str[i]]++
            
//         }
//         else{
//             dict[str[i]] = 1
//         }

        
        
        
//     }
//     for ( let j in dict ){
//         result += j;
//         result += dict[j];
//     }
//     if(result.length >= str.length){
//         console.log(str)
//         return str
//     }
//     console.log(result)
//     return result
//   }

// encodeStr(str1)



/* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {
    
    let numtemp = ""
    let strtemp = str[0]
    let result = ""
    for (let i = 1; i<=str.length;i++){

        if (isNaN(Number(str[i]))===false){
            // console.log("evaluated false, numtemp =" + numtemp)
            numtemp += String(str[i])
            // console.log("new numtemp =" + numtemp)
        }
        else if(i!=1){
            
            amount = Number(numtemp)
            for (let j=0; j < amount; j++){
                result += strtemp
                
            }
            numtemp =""
            strtemp = str[i]

        }
        
        else{            
            strtemp = str[i]

        }
        console.log(result)
    }
}

decodeStr(str1)