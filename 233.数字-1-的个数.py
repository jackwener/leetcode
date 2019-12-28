#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#

# @lc code=start
class Solution:
    def countDigitOne(self, n):
        cnt, i = 0, 1
        while i <= n: # i 依次个十百位的算，直到大于 n 为止。
            cnt += n // (i * 10) * i + min(max(n % (i * 10) - i + 1, 0), i)
            i *= 10
        return cnt
        
# @lc code=end

