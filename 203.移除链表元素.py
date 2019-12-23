#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next != None:
            if pre.next.val == val:
                pre.next=pre.next.next
                continue
            pre = pre.next

        return dummy.next

# @lc code=end

