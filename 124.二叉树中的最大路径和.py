#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (38.34%)
# Likes:    293
# Dislikes: 0
# Total Accepted:    22.8K
# Total Submissions: 58.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出: 6
# 
# 
# 示例 2:
# 
# 输入: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出: 42
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
            self.res = float("-inf")
            def helper(root):
                if not root: return 0
                # 左边最大值
                left = helper(root.left)
                # 右边最大值
                right = helper(root.right)
                # 和全局变量比较
                self.res = max(left + right + root.val, self.res)
                # >0 说明都能使路径变大
                return max(0, max(left,  right) + root.val)
            helper(root)
            return self.res 
        
# @lc code=end

