#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def helper(root,map):
            if not root: return 0
            sum = root.val + helper(root.left,map) + helper(root.right,map)
            if sum not in map:
                map[sum] = 1
            else:
                map[sum] += 1
            return sum
        map = {}
        helper(root,map)
        max_time = 0
        for time in map.values():
            max_time = max(time,max_time)
        res = []
        for num, time in map.items():
            if time == max_time:
                res.append(num)
        return res

# @lc code=end

