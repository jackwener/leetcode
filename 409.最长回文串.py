#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        res = 0
        flag = False
        for v in c.values():
            if v % 2 == 1: flag = True
            res += v // 2 * 2
        return res + 1 if flag else res
# @lc code=end

