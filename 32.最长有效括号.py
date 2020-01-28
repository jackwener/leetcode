#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (28.85%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 121.3K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if(not s):
            return 0
        # -1很重要，意味栈中元素表示上一不匹配位置索引。一旦匹配不到时，要把那个位置push
        stack=[-1]
        res=0
        for i in range(len(s)):
            if(s[i]=="("):
                stack.append(i)
            else:
                stack.pop()
                if(not stack):
                    # 一旦匹配不到时，要把那个位置push
                    stack.append(i)
                else:
                    res=max(res,i-stack[-1])
        return res
# @lc code=end

