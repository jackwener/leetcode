#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        a = {}
        for i in arr:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1

        b = {}
        for j in a.values():
            if j not in b.keys():
                b[j] = 1
            else:
                return False
        
        return True

# @lc code=end

