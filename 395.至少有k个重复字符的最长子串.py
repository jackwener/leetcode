#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#

# @lc code=start
from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(s, k):
            if len(s) < k: return 0
            short = [c for c, v in Counter(s).items() if v < k]
            if not short: return len(s)

            res = 0
            pre = -1
            for i, c in enumerate(s):
                if c in short:
                    res = max(res, helper(s[pre+1:i], k))
                    pre = i
                elif i == len(s) - 1:
                    res = max(res, helper(s[pre+1:], k))
            return res

        return helper(s,k)                
            

            

            
# @lc code=end

