#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0
    def findTilt(self, root: TreeNode) -> int:
        def find_sum(node):
            if not node: return 0
            left = find_sum(node.left)
            right = find_sum(node.right)
            self.res += abs(left - right)
            return left + right + node.val
        find_sum(root)
        return self.res
# @lc code=end

