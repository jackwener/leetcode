#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (62.69%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 53.5K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 
# 示例 1:
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2:
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head 

        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        middle, slow.next = slow.next, None

        left, right = self.sortList(head), self.sortList(middle)

        tmp_head = tmp = ListNode(0)
        while left and right:
            if left.val < right.val: 
                tmp.next = left
                left = left.next
                tmp = tmp.next
            else: 
                tmp.next = right
                right = right.next
                tmp = tmp.next
        tmp.next = left or right
        return tmp_head.next
        
# @lc code=end

