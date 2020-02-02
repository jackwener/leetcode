#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (48.31%)
# Likes:    1555
# Dislikes: 0
# Total Accepted:    150.4K
# Total Submissions: 307.9K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 示例:
# 
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
# 
# 进阶:
# 
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''method 1 dp
        size = len(nums)
        dp = [0]*size
        res = nums[0]
        for i in range(size):
            dp[i]=max(dp[i-1],0)+nums[i]
            res=max(dp[i],res)
        return res
        '''
        ans = nums[-1]
        sum = 0
        for num in nums:
            if sum < 0:
                sum = num
            else:
                sum += num
            ans = max(sum,ans)
        return ans
# @lc code=end

