#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        add = 0
        while n > 0:
            digit = n % 10
            n //= 10
            add += digit
            mul *= digit
        return mul - add
# @lc code=end

