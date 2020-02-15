#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def travel(node, level):
            if not node: return
            if len(res) - 1 < level: res.append([])
            res[level].append(node.val)
            travel(node.left, level + 1)
            travel(node.right, level + 1)
        travel(root,0)
        for i in range(1,len(res),2):
            res[i].reverse()
        return res
# @lc code=end

