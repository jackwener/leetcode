#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dp(self, root):
        if not root: return [0,0]
        l = self.dp(root.left)
        r = self.dp(root.right)

        return [root.val + l[1] + r[1], max(l) + max(r)]
    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))
# @lc code=end

