#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # nums = []
        # node = head
        # while node != None :
        #     nums.append(node.val)
        #     node = node.next

        # stack = []
        # stack_loc = []
        # res = [0] * len(nums)

        # for i in range(len(nums)):
        #     while stack and stack[-1] < nums[i]:
        #         res[stack_loc[-1]] = nums[i]
        #         stack.pop()
        #         stack_loc.pop()
        #     stack.append(nums[i])
        #     stack_loc.append(i)
        
        stack = []
        stack_loc = []
        loc = -1
        res = []
        while head:
            loc += 1
            res.append(0)
            while stack and stack[-1] < head.val:
                res[stack_loc[-1]] = head.val
                stack.pop()
                stack_loc.pop()
            stack.append(head.val)
            stack_loc.append(loc)
            
            head = head.next

        return res  
# @lc code=end

