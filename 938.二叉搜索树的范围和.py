#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
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
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if not node: return
            if node.val < L:
                dfs(node.right)
            elif node.val > R:
                dfs(node.left)
            else:
                self.res += node.val
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.res
# @lc code=end

