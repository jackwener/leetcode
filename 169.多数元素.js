/*
 * @lc app=leetcode.cn id=169 lang=javascript
 *
 * [169] 多数元素
 */

// @lc code=start
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    if(nums.length == 1) return nums[0];
    let map = {},result
    for(let num of nums){
        if(map.hasOwnProperty(num)){
            map[num]++;
            if(map[num] > nums.length/2){
                result = num;
            }
        }else{
            map[num] = 1;
        }
    }
    return result;  
};

// @lc code=end

