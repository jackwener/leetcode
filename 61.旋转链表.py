#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        length = 1
        count_head = head
        while count_head.next != None:
            length += 1
            count_head = count_head.next

        count_head.next = head
        k = k % length
        
        count = length - k

        while count != 1:
            head = head.next
            count = count -1
        result = head.next
        head.next = None
        return result

            
# @lc code=end

