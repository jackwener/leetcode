#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones):
        import heapq
        heap = []
        for i in stones:
            heapq.heappush(heap, i*-1)
        left_stones = len(stones)
        while left_stones > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, first-second)
                left_stones -= 1
            else:
                left_stones -= 2
        if left_stones == 1:
            return heapq.heappop(heap) * (-1)
        else:
            return 0

# @lc code=end

