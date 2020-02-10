/*
 * @lc app=leetcode.cn id=168 lang=javascript
 *
 * [168] Excel表列名称
 */

// @lc code=start
/**
 * @param {number} n
 * @return {string}
 */


var convertToTitle = function(n) {
    let res = "";
    while(n > 0){
        let num = n % 26
        n = Math.floor(n/26)
        if(num == 0){
            num = 26;
            n--;
        }
        res = String.fromCharCode(num+64)+res;
    }
    return res
};
// @lc code=end

