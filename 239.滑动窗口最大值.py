#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n<=1: return nums
        res = [0]*n
        if n <= k: return [max(nums)]
        res[k-1] = max(nums[:k])
        for i in range(k,n):
            if res[i-1] != nums[i-k]:
                res[i] = max(res[i-1],nums[i])
            else:
                res[i] = max(nums[i+1-k:i+1])
        return res[k-1:]

# @lc code=end

