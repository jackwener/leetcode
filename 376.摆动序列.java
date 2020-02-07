/*
 * @lc app=leetcode.cn id=376 lang=java
 *
 * [376] 摆动序列
 */

// @lc code=start
class Solution {
    public int wiggleMaxLength(int[] nums) {
        if (nums.length < 1) {
            return 0;
        }
        int lastDir = 0;
        int suc = 1;
        int start = 0;
        int lastValidValue = nums[0];
        for (start = 1; start < nums.length; start++) {
            if (nums[start] != nums[start - 1]) {
                lastDir = nums[start] > nums[start - 1] ? 1 : -1;//斜率
                lastValidValue = nums[start];
                suc=suc+1;
                break;
            }
        }


        for (; start < nums.length; start++) {
            if (-1 * lastDir * (nums[start] - nums[start - 1]) > 0) {
                suc++;
                lastDir = -1 * lastDir;
            } lastValidValue = nums[start];
        }
        return suc;
    }
}
// @lc code=end

