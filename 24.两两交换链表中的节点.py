#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        # 获得第 2 个节点
        next = head.next
        # 第1个节点指向第 3 个节点，并从第3个节点开始递归
        head.next = self.swapPairs(next.next)
        # 第2个节点指向第 1 个节点
        next.next = head
        # 或者 [head.next,next.next] = [swapPairs(next.next),head]
        return next

        
# @lc code=end

