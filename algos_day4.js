function longestPalindrome(str){
    let palindrome = true;
    let newStr = "";
    for(let i = 0; i<str.length;i++){
        palindrome === true;
        for(j = 1; palindrome === true; j++){
            if(i == 0){
                newStr = str[i];
                palindrome === false;
            }
            else if(str[i+j] === str[i-j]){
                continue
            }
            else{
                newStr = str[i]
            }
        }
    }
}