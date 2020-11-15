/*
 * @lc app=leetcode.cn id=165 lang=java
 *
 * [165] 比较版本号
 */

// @lc code=start
class Solution {
    public int compareVersion(String version1, String version2) {
        int num1 = 0, num2 = 0;
        int i = 0, j = 0;
        while (i < version1.length() || j < version2.length()) {
            while (i < version1.length() && version1.charAt(i) != '.') {
                num1 = num1 * 10 + (int) version1.charAt(i) - 48;
                i++;
            }
            while (j < version2.length() && version2.charAt(j) != '.') {
                num2 = num2 * 10 + (int) version2.charAt(j) - 48;
                j++;
            }

            System.out.printf("%d %d", num1, num2);

            if (num1 != num2) {
                return num1 > num2 ? 1 : -1;
            } else {
                num1 = 0;
                num2 = 0;
                i++;
                j++;
            }
        }
        return 0;
    }
}
// @lc code=end
