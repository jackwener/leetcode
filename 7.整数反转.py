#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (33.29%)
# Likes:    1562
# Dislikes: 0
# Total Accepted:    245.5K
# Total Submissions: 736K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0 
        elif x < 0:
            result = 0
            x = -x
            while x // 10 != 0:
                result = result*10 + x%10
                x = x//10
            result = result*10 + x%10
            if result >= 2 ** 31: return 0
            return -result
        else:
            result = 0
            while x // 10 != 0:
                result = result*10 + x%10
                x = x//10
            result = result*10 + x%10
            if result >= 2 ** 31: return 0
            return result


# @lc code=end

