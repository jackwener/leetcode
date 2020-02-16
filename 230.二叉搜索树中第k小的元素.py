#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#    def kthSmallest(self, root: TreeNode, k: int) -> int:
#         ''' method 1
#         nums = []
#         def helper(root,nums):
#             if not root: return
#             helper(root.left,nums)
#             nums.append(root.val)
#             helper(root.right,nums)
#         helper(root,nums)
#         return nums[k-1]
#         '''
        
class Solution:
    def mid_order(self, root):
        if not root: return
        yield from self.mid_order(root.left)
        yield root.val
        yield from self.mid_order(root.right)
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        gen = self.mid_order(root)
        for _ in range(k - 1):
            next(gen)
        return next(gen)


# @lc code=end

