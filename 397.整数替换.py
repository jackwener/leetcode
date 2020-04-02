#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#

# @lc code=start
# class Solution:
#     def integerReplacement(self, n: int) -> int:
#         deep = 0
#         from collections import deque
#         queue = deque()
#         queue.appendleft(n)
#         while queue:
#             for _ in range(len(queue)):
#                 node = queue.pop()
#                 if node == 1: return deep
#                 if node % 2 == 0: queue.appendleft(node//2)
#                 else:
#                     queue.appendleft(node - 1)
#                     queue.appendleft(node + 1)
#             deep += 1

class Solution:
    def integerReplacement(self, n: int) -> int:
        step = 0
        while n > 1:
            if n & 1 == 0: n >>= 1
            elif (n + 1) % 4 == 0 and n != 3: n += 1
            else:
                n -= 1
            step += 1
        return step
    
# @lc code=end

