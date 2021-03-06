#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (47.39%)
# Likes:    746
# Dislikes: 0
# Total Accepted:    42.9K
# Total Submissions: 90.2K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height: return 0
        # n = len(height)

        # left,right = 0, n - 1  # 分别位于输入数组的两端
        # maxleft,maxright = height[0],height[n - 1]
        # ans = 0

        # while left <= right:
        #     maxleft = max(height[left],maxleft)
        #     maxright = max(height[right],maxright)
        #     if maxleft < maxright:
        #         ans += maxleft - height[left]
        #         left += 1
        #     else:
        #         ans += maxright - height[right]
        #         right -= 1

        # return ans
        stack = []
        maxstack = 0
        res = 0
        for i in range(len(height)):
            h = height[i]
            if not stack:
                if h == 0:
                    continue
                else:
                    stack.append([h, i])
                    maxstack = max(maxstack, h)
            else:
                if h >= maxstack:
                    while stack:
                        last, lastid = stack.pop(-1)
                        res += (maxstack - last) # * (i - lastid)
                    maxstack = max(maxstack, h)
                stack.append([h, i])
        last = 0
        while stack:
            tmp, tmpid = stack.pop(-1)
            if tmp < last:
                res += last - tmp
            last = max(last, tmp)
        return res

      
# @lc code=end

