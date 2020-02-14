#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        parent = [-1] * len(M)

        def find(parent, i):
            if parent[i] == -1: return i
            return find(parent, parent[i])
        
        def union(parent, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if xroot != yroot:
                parent[xroot] = yroot
        
        def union_find(Matrix):
            for i in range(len(Matrix)):
                for j in range(len(Matrix)):
                    if Matrix[i][j] == 1 and i != j:
                        union(parent, i, j)
            count = 0
            for i in range(len(parent)):
                if parent[i] == -1:
                    count += 1
            return count
        
        return union_find(M)



# @lc code=end

