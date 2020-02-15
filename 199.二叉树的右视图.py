#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
        self.res = []
    def rightSideView(self, root: TreeNode) -> List[int]:
        def helper(node, level):
            if not node: return
            if level == len(self.res): self.res.append(node.val)
            helper(node.right,level+1)
            helper(node.left,level+1)
        helper(root, 0)
        return self.res
            
# @lc code=end

