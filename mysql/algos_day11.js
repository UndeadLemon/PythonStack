

// const queue1 = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1];
// const expected1 = false;

// const queue2 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected2 = true;

// const queue3 = [1, 0, 0, 0, 0, 0, 0, 0, 1];
// const expected3 = true;

// const queue4 = [];
// const expected4 = true;


// function socialDistancing(arr){
//     let distance = 6
//     for(let i= 1; i < arr.length; i++){
//         if(arr[i] === 1){
//             if (distance < 6){
//                 return false
//             }
//             distance = 0
//         }
//         if(arr[i] === 0){
//             distance++
//         }
//     }
//     return true
// }



/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
   
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

const nums3 = [13,5,90,18]
const expected3 = 2

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
 const test1 = [1, 1, 1, 1, 1, 5, 1, 1, 1, 2, 3, 2, 67, 5,5,5,5]
function balanceIndex(nums) {
    let leftcount = 0
    let rightcount = 0
    let k = nums.length-1
    let i = 0
    let j = 0
    let isOdd = 0
    if (nums.length < 3){
        return -1
    }


    while(i-1<k){
        j++

        // console.log("indexcount is :" + ((i) -k))
        // console.log("difference is :" + (leftcount-rightcount))
        if(leftcount == rightcount && i != 0 && (j == nums.length || j == nums.length -1)) {
            return i
        }
        if(leftcount<=rightcount){
            leftcount += nums[i]
            console.log("leftcount is:" + leftcount)
            i++
            
        }
        else{
            rightcount += nums[k]
            k--
            
            console.log("rightcount is:" + rightcount)
        }
        
    }
    return -1
}
console.log(balanceIndex(nums3))

// console.log(socialDistancing(queue4))