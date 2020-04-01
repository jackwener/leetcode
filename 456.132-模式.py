#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132模式
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 2: return False

        min_ = [0] * length
        min_[0] = nums[0]
        for i in range(1, length):
                min_[i] = min_(nums[i], min_[i-1])

        stack = []
        tmp = 0
        for i in range(length - 1, -1, -1):
            # if nums[i]>mi[i]:
            #     while stack and mi[i]>=stack[-1]:
            #         stack.pop()
                
            #     if stack and stack[-1]<nums[i]:
            #         return True
            #     stack.append(nums[i])
            while stack and stack[-1] < nums[i]:
                tmp = stack.pop()
            if min_[i] > stack:
                return True
            stack.append(nums[i])
        return False

# @lc code=end

