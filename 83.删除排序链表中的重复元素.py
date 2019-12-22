#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        exist = {
            head.val: True,
        }
        pre = head
        cur = head.next
        while cur != None :
            if cur.val in exist:
                pre.next = cur.next
                cur = cur.next
            else:
                exist[cur.val] = True
                pre = pre.next
                cur = cur.next
        return head

# @lc code=end

