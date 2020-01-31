#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (40.96%)
# Likes:    256
# Dislikes: 0
# Total Accepted:    40.5K
# Total Submissions: 97.9K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 示例 1:
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 说明：
# 
# 
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len_one = len(num1)
        len_two = len(num2)
        list = [0]*(len_one+len_two)

        for i in range(1,len_one+1):
            num1Val = int(num1[-i]);
            for j in range(1,len_two+1):
                num2Val = int(num2[-j])
                sum = list[-(i + j - 1)] + num1Val * num2Val
                list[-(i + j - 1)] = sum % 10 
                list[-(i + j)] += sum // 10


        result = ""
        start = len_one+len_two-1
        for i in range(len_one+len_two):
            if list[i] != 0:
                start = i
                break
        
        for i in range(start,len_one+len_two):
            result += str(list[i])

        return result
# @lc code=end

