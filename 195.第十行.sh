#
# @lc app=leetcode.cn id=195 lang=bash
#
# [195] 第十行
#

# @lc code=start
# Read from the file file.txt and output the tenth line to stdout.

# tail -n +10 file.txt | head -1

awk "NR == 10" file.txt

# @lc code=end

