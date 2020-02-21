#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        if len(arr)<3:
            return [arr]

        min_diff = arr[1] - arr[0]
        res = [arr[0:2]]
        for i in range(2,len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                res.append([arr[i - 1], arr[i]])
            elif arr[i] - arr[i - 1] < min_diff:
                min_diff = arr[i] - arr[i - 1]
                res = [[arr[i - 1], arr[i]]]
        return res


# @lc code=end

