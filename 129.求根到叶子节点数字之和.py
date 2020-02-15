#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
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
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node,tmp):
            if not node: return 0
            if not node.left and not node.right: self.res += tmp*10 + node.val
            helper(node.left,tmp*10 + node.val)
            helper(node.right,tmp*10 + node.val)
        helper(root,0)
        return self.res

# @lc code=end

