#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (37.09%)
# Likes:    412
# Dislikes: 0
# Total Accepted:    49.9K
# Total Submissions: 133.8K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp N^2复杂度 超时
        # n = len(nums)
        # dp = [0]*n
        # dp[-1] = 1
        # for i in range(n-2,-1,-1):
        #     if nums[i]==0: continue
        #     for j in range(i+nums[i],i,-1):
        #         if j > n-1: 
        #             dp[i]=1
        #             break
        #         else:
        #             if dp[j]==1:
        #                 dp[i]=1
        #                 break
        # return dp[0]
        last = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= last-i:
                last = i
        return last == 0

                    

# @lc code=end

