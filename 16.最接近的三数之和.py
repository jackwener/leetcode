#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        if n < 3: return None
        res = nums[0] + nums[1] + nums[2]       
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right :
                cur = nums[i] + nums[left] + nums[right]
                if cur == target:return target
                if abs(res-target) > abs(cur-target):
                    res = cur
                if cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
        return res

# @lc code=end

