#
# @lc app=leetcode.cn id=768 lang=python3
#
# [768] 最多能完成排序的块 II
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            # 递增栈
            if not stack or stack[-1] <= num:
                stack.append(num)
            else:
                cur_max = stack.pop()
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(cur_max)
        return len(stack)
# @lc code=end

