#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (48.51%)
# Likes:    126
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 44.3K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 注意：
# 
# 
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        len_one,len_two,carry = len(num1),len(num2),0
        result = ""
        i = 0
        while i < len_one or i < len_two:
            n1 = int(num1[len_one - 1 - i]) if i < len_one else 0
            n2 = int(num2[len_two - 1 - i]) if i < len_two else 0
            n3 = (n1+n2+carry)%10
            carry = (n1+n2+carry) // 10
            result = str(n3) + result
            i += 1
        return "1" + result if carry > 0 else result
            

# @lc code=end

