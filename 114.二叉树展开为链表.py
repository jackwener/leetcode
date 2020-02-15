#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (66.44%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 33.8K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为链表。
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root == None: return
            helper(root.left)
            helper(root.right)
            if root.left != None: # 后序遍历
                pre = root.left # 令 pre 指向左子树
                while pre.right: pre = pre.right # 找到左子树中的最右节点
                pre.right = root.right # 令左子树中的最右节点的右子树 指向 根节点的右子树
                root.right = root.left # 令根节点的右子树指向根节点的左子树
                root.left = None # 置空根节点的左子树
        helper(root)
        
# @lc code=end

