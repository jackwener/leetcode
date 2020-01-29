#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (44.69%)
# Likes:    418
# Dislikes: 0
# Total Accepted:    110.6K
# Total Submissions: 246.3K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if len(nums) == 0:
        #     return 0            
        
        # start = 0
        # end = len(nums)-1
        # middle = (start + end + 1) // 2 
        # while start != end and end - start != 1:
        #     if nums[middle] > target:
        #         end = middle
        #         middle = (start + end + 1) // 2 
        #     elif nums[middle] < target:
        #         start = middle
        #         middle = (start + end + 1) // 2 
        #     else :
        #         return middle
        # if nums[end] < target:
        #     return end+1
        # if nums[start] >= target:
        #     return start
        # return start + 1
        size = len(nums)
        if size == 0:
            return 0

        # 特判
        if nums[size - 1] < target:
            return size

        left = 0
        right = size - 1

        while left < right:
            mid = (left + right) >> 1
            # 严格小于 target 的元素一定不是解
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                right = mid
        return left

# @lc code=end

