#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        l = len(nums)
        target = sum(nums)
        if target & 1 != 0: return False
        target //= 2
        dp=[[False]*(target+1) for _ in range(l)]
        dp[0][0] = True
        for i in range(1,l):
            for j in range(target+1):
                if j > nums[i]:
                    dp[i][j]=dp[i-1][j] or (dp[i-1][j-nums[i]])
                elif j == nums[i]:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i-1][j-nums[i]]
        return dp[-1][-1]
# @lc code=end

