#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adjacency = [[0] * numCourses for _ in range(numCourses)]
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre][cur] = 1
        for i in range(numCourses):
            if not indegrees[i]: queue.append(i)
        res = []
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            for cur in range(numCourses):
                if adjacency[pre][cur] == 1:
                    indegrees[cur] -= 1
                    if not indegrees[cur]: queue.append(cur)
        if len(res) != numCourses: return[]
        else: return res
# @lc code=end

