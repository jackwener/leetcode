/*
 * @lc app=leetcode.cn id=171 lang=javascript
 *
 * [171] Excel表列序号
 */

// @lc code=start
/**
 * @param {string} s
 * @return {number}
 */
var titleToNumber = function(s) {
    // var res = 0
    // for(i = s.length - 1; i >= 0; i--){
    //     num = s[i].charCodeAt() - 64
    //     res += num * Math.pow(26,s.length-i-1)
    // }
    // return res
    // let sum = 0, i = s.length - 1, carry = 1



    // while (i >= 0) {
    //     let cur = s[i].charCodeAt() - 64

    //     sum += cur * carry
    //     carry *= 26
    //     i--
    // }

    // return sum

    const map = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    var res = 0;
    var len = s.length;
    for(let c of s) {
        if(len > 1) {
            res += map.indexOf(c) * Math.pow(26, len - 1);
            len--;
        } else {
            res += map.indexOf(c);
        }
    }
    return res;

}
// @lc code=end

