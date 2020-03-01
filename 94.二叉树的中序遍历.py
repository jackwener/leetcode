#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # res = []
        # stack = []
        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         tmp = stack.pop()
        #         res.append(tmp.val)
        #         root = tmp.right
        # return res

        pre = None
        cur = root
        p = None
        res = []
        while cur != None:
            if cur.left != None:
                p = cur.left
                while p.right != None:
                    p = p.right
                p.right = cur
                cur = cur.left
                p.right.left = None
            else:
                res.append(cur.val)
                cur = cur.right

        return res


# @lc code=end

