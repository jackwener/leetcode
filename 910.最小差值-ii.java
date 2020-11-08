/*
 * @lc app=leetcode.cn id=910 lang=java
 *
 * [910] 最小差值 II
 */

// @lc code=start
class Solution {
    public int smallestRangeII(int[] A, int K) {
        int end = A.length - 1;
        Arrays.sort(A);
        int res = A[end] - A[0];
        for(int i = 0; i < end ; i++){
            int high = Math.max(A[i]+K, A[end]-K);
            int low = Math.min(A[i+1]-K, A[0]+K);
            res = Math.min(res, high - low);
        }

        return res;
    }
}

// @lc code=end

