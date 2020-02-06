#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0]*n
        min_dp = [0]*n
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1,n):
            if nums[i] < 0:
                max_dp[i] = max(min_dp[i-1] * nums[i],nums[i])
                min_dp[i] = min(max_dp[i-1] * nums[i],nums[i])
            else:
                max_dp[i] = max(max_dp[i-1] * nums[i],nums[i])
                min_dp[i] = min(min_dp[i-1] * nums[i],nums[i])            
        res = nums[0]
        for i in range(n):
            res = max(max_dp[i],res)
        return res
# @lc code=end

