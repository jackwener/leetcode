#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        l = len(num)
        if l == k: return "0"
        # 维护一个单调增的队列
        stack = []
        cnt = k
        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1
            stack.append(n)
        return str(int("".join(stack[:l - cnt])))


# @lc code=end

