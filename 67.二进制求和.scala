/*
 * @lc app=leetcode.cn id=67 lang=scala
 *
 * [67] 二进制求和
 *
 * https://leetcode-cn.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (51.52%)
 * Likes:    294
 * Dislikes: 0
 * Total Accepted:    59.7K
 * Total Submissions: 114.7K
 * Testcase Example:  '"11"\n"1"'
 *
 * 给定两个二进制字符串，返回他们的和（用二进制表示）。
 * 
 * 输入为非空字符串且只包含数字 1 和 0。
 * 
 * 示例 1:
 * 
 * 输入: a = "11", b = "1"
 * 输出: "100"
 * 
 * 示例 2:
 * 
 * 输入: a = "1010", b = "1011"
 * 输出: "10101"
 * 
 */

// @lc code=start
object Solution {
    import scala.math.min
    def addBinary(a: String, b: String): String = {
        int lenA = a.length()
        int lenB = a.length()
        val buf = new StringBuilder;
        int carry = 0
        int lenMin = min(lenA,lenB)
        for(i <-1 to lenMin){
            int sum = carry
            sum += lenA - i >= 0 ? a.charAt(lenA - i) - '0' : 0
            sum += lenB - i >= 0 ? b.charAt(lenB - i) - '0' : 0
            ans.append(sum % 2)
            carry = sum / 2
        }
        ans.append(carry == 1 ? carry : "")
        return ans.reverse().toString()
    }
}
// @lc code=end

