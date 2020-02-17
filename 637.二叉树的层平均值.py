#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        d = collections.defaultdict(list)
        def f(r, i):
            if r:
                d[i] += [r.val]
                f(r.left,i + 1)
                f(r.right,i + 1)
        f(root, 0)
        return [sum(vals) / len(vals) for vals in d.values()]

# @lc code=end

