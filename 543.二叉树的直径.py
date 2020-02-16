#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0
        def helper(root):
            if not root: return 0;
            left_depth = helper(root.left)
            right_depth = helper(root.right)
            self.max = max(self.max, left_depth + right_depth)
            return max(left_depth, right_depth) + 1
        helper(root)
        return self.max
# @lc code=end

