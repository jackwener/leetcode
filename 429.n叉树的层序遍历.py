#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return []
        res = []
        
        def bfs(root):
            queue = [root]
            while queue:
                nxt = []
                tmp = []
                for node in queue:
                    tmp.append(node.val)
                    for ch in node.children:
                        nxt.append(ch)
                res.append(tmp)
                queue = nxt
        
        bfs(root)
        return res

# @lc code=end

