#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.29%)
# Likes:    361
# Dislikes: 0
# Total Accepted:    38.3K
# Total Submissions: 117.6K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        decrease_flag = True

        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                decrease_flag = False
                for j in range(i,len(nums)):
                    if j == len(nums)-1:
                        tmp = nums[i-1]
                        nums[i-1]=nums[-1]
                        nums[-1]=tmp
                        self.reverse(nums,i,len(nums)-1)
                        return
                    if nums[j+1] <= nums[i-1]:
                        tmp = nums[i-1]
                        nums[i-1]=nums[j]
                        nums[j]=tmp
                        self.reverse(nums,i,len(nums)-1)
                        return
        if decrease_flag:
            nums.reverse()
    def reverse(self,nums, i, j):
        while i < j:
            nums[i],nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
# @lc code=end

