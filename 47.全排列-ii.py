#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (55.97%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    31.6K
# Total Submissions: 56.4K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()
        def backtrack(nums, tmp):
            if len(nums) == len(tmp):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i in visited or (i > 0 and i - 1 not in visited and nums[i-1] == nums[i]):
                    continue
                visited.add(i)
                backtrack(nums, tmp + [nums[i]])
                visited.remove(i)
        backtrack(nums, [])
        return res

# @lc code=end

