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
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []
        res.append(root.val)
        if not root.right:
            res += self.rightSideView(root.right)
        elif root.left:
            res += self.rightSideView(root.left)
        else:
            return [root.val]
        
        return self.rightSideView(root)

            
# @lc code=end

