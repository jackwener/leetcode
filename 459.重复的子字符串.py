#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        next = [-1] * n
        for i in range(1,n):
            j = next[i-1]
            while j >= 0 and s[j+1] != s[i]:
                j = next[j]
            if s[j+1] == s[i]:
                next[i] = j + 1
        return next[-1] >= 0 and n % (n - 1 - next[-1]) == 0

# @lc code=end

