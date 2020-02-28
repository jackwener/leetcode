#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#

# @lc code=start
# class Solution:
#     def sumSubarrayMins(self, A):
#         n = len(A)
#         if n == 0:
#             return 0
#         if n == 1:
#             return A[0]
        
#         ans = 0
#         left = [0] * n
#         right = [0] * n
        
#         stack = []
#         for i in range(n):
#             while stack and A[stack[-1]] > A[i]:
#                 stack.pop()
#             if not stack:
#                 left[i] = -1
#             else:
#                 left[i] = stack[-1]
#             stack.append(i)
        
#         stack = []
#         for i in range(n - 1, -1, -1):
#             while stack and A[stack[-1]] >= A[i]:
#                 stack.pop()
#             if not stack:
#                 right[i] = n
#             else:
#                 right[i] = stack[-1]
#             stack.append(i)
        
#         for i in range(n):
#             ans += (i - left[i]) * (right[i] - i) * A[i]
#             ans %= 1000000007
#         return ans

class Solution:
    def sumSubarrayMins(self, A):
        ans = 0
        A = [float('-inf')] + A + [float('-inf')]
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] > a:
                cur = stack.pop()
                ans += A[cur] * (i-cur) * (cur-stack[-1])
            stack.append(i)
        return ans % (10**9 + 7)

        

# @lc code=end

