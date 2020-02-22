#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        val = root.val
        def helper(root, val):
            if not root: return True
            if root.val != val: return False
            return helper(root.left, val) and helper(root.right, val)
        return helper(root, val)
        
# @lc code=end

