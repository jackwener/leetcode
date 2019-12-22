#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
        }
        result = []

        if digits != "":
            char = digits[0]
            for char_phone in phone[char]:
                pre_result = self.letterCombinations(digits[1:])
                for str_in in pre_result:
                    result.insert(char_phone+str_in)
            return result
        else:
            return 
        # @lc code=end

