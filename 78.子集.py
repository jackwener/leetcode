#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (75.65%)
# Likes:    451
# Dislikes: 0
# Total Accepted:    56.5K
# Total Submissions: 74.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        n = len(nums)

        def backtrack(start,list):
            res.append(list[:])
            for i in range(start,n):
                list.append(nums[i])
                backtrack(i+1,list)
                list.pop()
        backtrack(0,[])
        return res
# @lc code=end

