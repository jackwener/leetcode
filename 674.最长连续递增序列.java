/*
 * @lc app=leetcode.cn id=674 lang=java
 *
 * [674] 最长连续递增序列
 */

// @lc code=start
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        if(nums.length == 0) return 0;
        int res = 0, start = 0, end = 0;

        for(int i = 1; i < nums.length; i++){
            if(nums[i] > nums[i-1]){
                end = i;
            } else {
                res = Math.max(end - start + 1, res);
                start = i;
            }
        }
        res = Math.max(end - start + 1, res);
        return res;
    }
}
// @lc code=end

