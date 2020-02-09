#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ''' 
        copy method
    
        nums = []
        while head != None:
            nums.append(head.val)
            head  = head.next
        left = 0
        right = len(nums)-1
        while left < right :
            if nums[left] != nums[right]:
                return False
            else:
                left, right = left + 1, right - 1
        return True
        '''
# @lc code=end

