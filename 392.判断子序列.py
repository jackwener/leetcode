#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        s_len = len(s)
        t_len = len(t)
        s_st = 0
        t_st = 0
        while s_st != s_len and t_st != t_len:
            if s[s_st] != t[t_st]:
                t_st += 1
            else:
                s_st,t_st = s_st+1,t_st+1
        return s_st == s_len
# @lc code=end

