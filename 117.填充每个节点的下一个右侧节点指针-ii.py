#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # if not root: return None
        # queue = []
        # queue.append(root)
        # while queue:
        #     n = len(queue)
        #     pre = queue.pop(0)
        #     if pre.left: queue.append(pre.left)
        #     if pre.right: queue.append(pre.right)
        #     for _ in range(1,n):
        #         node = queue.pop(0)
        #         pre.next = node
        #         if node.left: queue.append(node.left)
        #         if node.right: queue.append(node.right)
        #         pre = node
        # return root


        # from collections import deque
        # if not root: return root
        # queue = deque()
        # queue.appendleft(root)
        # while queue:
        #     p = None
        #     n = len(queue)
        #     for _ in range(n):
        #         tmp = queue.pop()
        #         if p:
        #             p.next = tmp
        #             p = p.next
        #         else:
        #             p = tmp
        #         if tmp.left:
        #             queue.appendleft(tmp.left)
        #         if tmp.right:
        #             queue.appendleft(tmp.right)
        #     p.next = None 
        # return root       


        cur = root
        head = None
        tail = None
        while cur:
            while cur:
                if cur.left:
                    if not head:
                        head = cur.left
                        tail = cur.left
                    else:
                        tail.next = cur.left
                        tail = tail.next
                if cur.right:
                    if not head:
                        head = cur.right
                        tail = cur.right
                    else:
                        tail.next = cur.right
                        tail = tail.next
                cur = cur.next
            cur = head
            head = None
            tail = None
        return root

        

# @lc code=end

