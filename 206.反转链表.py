#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # pre = None
        # cur = head
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
            
        #     pre = cur
        #     cur = tmp        
        # return pre

        '''
        method 2
        '''
        if head == None:
            return None
        if  head.next == None :
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


# @lc code=end

