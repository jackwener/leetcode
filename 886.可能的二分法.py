#
# @lc app=leetcode.cn id=886 lang=python3
#
# [886] 可能的二分法
#

# @lc code=start
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        father = [0] * (N+1)
        for i in range(1,N+1):
            father[i] = i

        def find(x): #寻找根节点
            if x != father[x]:
                father[x] = find(father[x]) #路径压缩
            return father[x]

        for i in range(len(dislikes)):
            x = find(dislikes[i][0])
            y = find(dislikes[i][1])
        if x == y: return False
        else:
            father[a] = y
            father[b] = x
        return True






# @lc code=end

