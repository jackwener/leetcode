#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (34.72%)
# Likes:    318
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 61.6K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        count = Counter(t)
        left = 0
        n = 0
        res_len = float('inf')
        ans = ""
        for right, char in enumerate(s):
            if char not in count: continue
            count[char] -= 1
            if count[char] == 0: n += 1
            while s[left] not in count or count[s[left]] < 0:
                if s[left] in count: count[s[left]] += 1
                left += 1
            if n == len(count):
                if not ans or len(ans) > right - left + 1:
                    ans = s[left: right+1]

        return ans

# @lc code=end

