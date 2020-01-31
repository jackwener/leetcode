#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (67.52%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    51.4K
# Total Submissions: 76.1K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0: return []
        dict = {}
        for i in range(1,target+1):
            dict[i]=[]
        
        for i in range(1,target+1):
            for j in candidates:
                if i==j:
                    dict[i].append([i])
                elif i>j:
                    for k in dict[i-j]:
                        x = k[:]
                        x.append(j)
                        x.sort() # 升序，便于后续去重
                        if x not in dict[i]:
                            dict[i].append(x)

        return dict[target]


# @lc code=end

