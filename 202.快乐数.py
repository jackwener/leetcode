#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            sum = 0
            while n > 0:
                bit = n % 10
                sum += bit * bit
                n = n // 10
            return sum

        slow, fast = n, n
        while True:
            slow = helper(slow)
            fast = helper(fast)
            fast = helper(fast)
            if slow == fast:
                break
        
        return slow == 1



# @lc code=end

