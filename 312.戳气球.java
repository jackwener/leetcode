/*
 * @lc app=leetcode.cn id=312 lang=java
 *
 * [312] 戳气球
 */

// @lc code=start
class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length + 2;
        int[] A = new int[n];
        A[0] = A[n - 1] = 1;
        for (int i = 1; i < n - 1; i++) {
            A[i] = nums[i - 1];
        }

        int[][] dp = new int[n][n];
        
        for (int i = 0; i < n - 1; i++) {
            dp[i][i + 1] = 0;
        }

        for (int len = 1; len <= n - 2; len++) {
            for (int i = 1; i <= n - 2 - len ; i++) {
                int j = i + len - 1;
                dp[i][j] = Integer.MIN_VALUE;
                //枚举中间的气球
                for (int k = i; k <= j ; k++) {
                    dp[i][j] = Math.max(dp[i][j], dp[i][k-1] + dp[k+1][j] + A[i-1] * A[k] * A[j+1]);
                }
            }
        }
        return dp[1][n - 2];
    }
}


// @lc code=end

