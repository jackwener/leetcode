#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (71.59%)
# Likes:    208
# Dislikes: 0
# Total Accepted:    31.9K
# Total Submissions: 44.1K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 
# 示例:
# 
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start,tmp_list):
            if len(tmp_list) == k:
                res.append(tmp_list[:])
            for i in range(start,n+1):
                tmp_list.append(i)
                backtrack(i+1,tmp_list)
                tmp_list.pop()

        backtrack(1,[])
        return res
# @lc code=end

