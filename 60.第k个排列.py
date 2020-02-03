#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#
# https://leetcode-cn.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (47.58%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    21.6K
# Total Submissions: 44.8K
# Testcase Example:  '3\n3'
#
# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
# 
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# 给定 n 和 k，返回第 k 个排列。
# 
# 说明：
# 
# 
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 
# 
# 示例 1:
# 
# 输入: n = 3, k = 3
# 输出: "213"
# 
# 
# 示例 2:
# 
# 输入: n = 4, k = 9
# 输出: "2314"
# 
# 
#

# @lc code=start
class Solution(object):
    def getPermutation(self, n, k):
        #阶乘
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

        res=""
        #用列表存储剩余数字
        remain=list(range(1,n+1))
        turn=n-1
        rem=k-1
        #每一轮根据求商得到的坐标，取出该位置的数字
        while turn>0:
            div=factorial(turn)
            ind=rem//div
            res+=str(remain[ind])
            del remain[ind]
            rem=rem%div
            turn-=1
        res+=str(remain[0])
        return res

# @lc code=end

