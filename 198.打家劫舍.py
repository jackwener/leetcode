#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        currMax = 0
        for x in nums:
            temp = currMax
            currMax = max(prevMax + x, currMax)
            prevMax = temp
    
        return currMax
# @lc code=end

