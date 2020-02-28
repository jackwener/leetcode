#
# @lc app=leetcode.cn id=477 lang=python3
#
# [477] 汉明距离总和
#

# @lc code=start
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bit_arr_zero = [0] * 31
        bit_arr_one = [0] * 31
        for num in nums:
            cnt = 0
            while cnt < 31:
                if num & 1 == 1: bit_arr_one[cnt] += 1
                else: bit_arr_zero[cnt] += 1
                cnt += 1
                num >>= 1
        ans = 0
        for i in range(31):  
            ans += bit_arr_zero[i] * bit_arr_one[i]
        return ans

# @lc code=end

