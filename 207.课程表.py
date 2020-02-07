#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adjacency = [[0] * numCourses for _ in range(numCourses)]
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre][cur] = 1
        for i in range(numCourses):
            if not indegrees[i]: queue.append(i)
        n = numCourses
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for i in range(n):
                if adjacency[pre][i] == 1:
                    indegrees[i] -= 1
                    if not indegrees[i]: queue.append(i)
        return not numCourses
                
# @lc code=end

