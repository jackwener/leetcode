#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
from math import isinf


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = b = c = float('-inf')

        for num in nums:
            if num > a:
                c = b
                b = a
                a = num
            elif num > b and num != a:
                c = b
                b = num
            elif num > c and num != b and num != a:
                c = num

        return a if isinf(c) else c

# @lc code=end

