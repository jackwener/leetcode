#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        residual = [0] * (n-1)
        for i in range(n-1):
            residual[i] = nums[i+1] - nums[i]
        res = n
        for i in range(n-2):
            if residual[i] * residual[i+1] >= 0:
                res -= 1
        if residual[-1]==0: res -= 1
        return res
# @lc code=end

