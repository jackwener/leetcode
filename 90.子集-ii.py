#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (57.92%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    20.3K
# Total Submissions: 34.7K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        
        def backtrack(start,list):
            res.append(list[:])
            for i in range(start,n):
                if i > start and nums[i]==nums[i-1]: continue
                list.append(nums[i])
                backtrack(i+1,list)
                list.pop()
        backtrack(0,[])
        return res
# @lc code=end

