#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (58.35%)
# Likes:    298
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 29.4K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过已填充的空格来解决数独问题。
# 
# 一个数独的解法需遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 空白格用 '.' 表示。
# 
# 
# 
# 一个数独。
# 
# 
# 
# 答案被标成红色。
# 
# Note:
# 
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# 
# 
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        num = []
        num.append("")
        num.append("1")
        if n==1: return num[1]
        for i in range(2,n+1):
            p = []
            s = ""
            for x in num[i-1]:
                if p==[] or x==p[0]:
                    p.append(x)
                else:
                    s += str(len(p))
                    s += p[0]
                    p = []
                    p.append(x)
            s += str(len(p))
            s += p[0]
            num.append(s)
        
        return num[n]

# @lc code=end

