#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# https://leetcode-cn.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (41.66%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    67.9K
# Total Submissions: 162.6K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
# 
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 
# 示例 1:
# 
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "race a car"
# 输出: false
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = ''
        s = s.lower()
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz0123456789':
                snew = snew + i
        snew = snew.lower()
        srnew = snew[::-1]
        if snew == srnew:
            return True
        else:
            return False

# @lc code=end

