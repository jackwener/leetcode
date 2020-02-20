import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=343 lang=java
 *
 * [343] 整数拆分
 */

// @lc code=start
class Solution {
    // public int integerBreak(int n) {
    //     if(n <= 3) return n - 1;
    //     int a = n / 3, b = n % 3;
    //     if(b == 0) return (int)Math.pow(3, a);
    //     if(b == 1) return (int)Math.pow(3, a - 1) * 4;
    //     return (int)Math.pow(3, a) * 2;

    public int integerBreak(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, 1);
        for (int i = 3; i <= n; ++i) {
            for (int  j = 1; j < i; ++j) {
                dp[i] = Math.max(dp[i], Math.max(j * (i - j), j * dp[i - j]));
            }
        }
        return dp[n];
    }
}

// @lc code=end

