#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution(object):
    def countBits(self, num):
        result = [0] * (num+1)
        for i in range(1,num+1):
            if 1 & i:
                result[i] = result[i>>1] + 1
            else:
                result[i] = result[i>>1]
        return result

# @lc code=end

