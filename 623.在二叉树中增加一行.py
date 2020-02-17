#
# @lc app=leetcode.cn id=623 lang=python3
#
# [623] 在二叉树中增加一行
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        queue = [root]
        d -= 2
        while d != 0:
            n = len(queue)
            d -= 1
            for i in range(n):
                p = queue.pop(0)
                if p.left: queue.append(p.left)
                if p.right: queue.append(p.right)
        n = len(queue)
        for i in range(n):
            if queue[i].left:
                node = TreeNode(v)
                node.left = queue[i].left
                queue[i].left = node
            else:
                queue[i].left = TreeNode(v)
            if queue[i].right:
                node = TreeNode(v)
                node.right = queue[i].right
                queue[i].right = node
            else:
                queue[i].right = TreeNode(v)
        return root

# @lc code=end

