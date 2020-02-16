#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        queue = [root]
        while queue:
            n = len(queue)
            max_tmp = float('-inf')
            for i in range(n):
                node = queue.pop(0)
                max_tmp = max(max_tmp, node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(max_tmp)
        return res


# @lc code=end

