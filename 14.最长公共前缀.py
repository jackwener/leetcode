#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""
        str_common = strs[0]
        for str_in in strs :
            str_common = self.common(str_in, str_common)
            if str_common == "":
                return ""
        return str_common


    def common(self,str1,str2) -> str:
        i = 0
        if str1=="" or str2=="":
            return ""
        if str1[0]!=str2[0]:
            return ""
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                i += 1
                continue
            else:
                return str1[:i]
        return str1[:i]
# @lc code=end

