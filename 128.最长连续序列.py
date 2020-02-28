#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (46.90%)
# Likes:    230
# Dislikes: 0
# Total Accepted:    24.1K
# Total Submissions: 50.8K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 
# 要求算法的时间复杂度为 O(n)。
# 
# 示例:
# 
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        class UnionFind():
            def __init__(self):
                self.father = {}
            
            def find(self, x):
                if self.father[x] != x:
                    self.father[x] = self.find(self.father[x])
                return self.father[x]

            def union(self, x):
                self.father[x] = x
                if x - 1 in self.father:
                    self.father[x - 1] = x
                if x + 1 in self.father:
                    self.father[x] = x + 1
            
        uf = UnionFind()
        for num in nums:
            uf.union(num)

        max_l = 0
        for num in nums:
            root = uf.find(num)
            l = root - num + 1
            if l > max_l:
                max_l = l

        return max_l

# @lc code=end

