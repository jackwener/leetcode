#
# @lc app=leetcode.cn id=685 lang=python3
#
# [685] 冗余连接 II
#

# @lc code=start
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        father = [i for i in range(len(edges)+1)]
        res = [0,0]
        def find(x):
            if father[x] != x:
                father[x] = find(father[x])
            return father[x]
        def union(x, y):
            x_f = find(x)
            y_f = find(y)
            if x_f == y_f:
                res[0], res[1] = x, y
            else:
                father[y_f] = x_f
            
        for edge in edges:
            union(edge[0], edge[1])

        return res

# @lc code=end

