#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}
        def dfs(root):
            if not root: return
            if root in lookup:
                return lookup[root]
            clone = Node(root.val,[])
            lookup[root] = clone
            for n in root.neighbors:
                clone.neighbors.append(dfs(n))            
            return clone
        return dfs(node)


# @lc code=end

