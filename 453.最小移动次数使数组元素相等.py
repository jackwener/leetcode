#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小移动次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        count = 0
        for num in nums:
            count += num - min_num
        return count
# @lc code=end

