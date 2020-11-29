/*
 * @lc app=leetcode.cn id=542 lang=java
 *
 * [542] 01 矩阵
 */

// @lc code=start
class Solution {
    public int[][] updateMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] res = new int[m][n];

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++){
                if(matrix[i][j] != 0)
                res[i][j] = 0x7fff0000;
            }
        }

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++){
                if(i != 0) res[i][j] = Math.min(res[i][j],res[i-1][j] + 1);
                if(j != 0) res[i][j] = Math.min(res[i][j],res[i][j-1] + 1);
            }
        }


        for(int i = m-1; i >= 0; i--) {
            for(int j = n-1; j >= 0; j--){
                if(i != m-1) res[i][j] = Math.min(res[i][j],res[i+1][j]+1);
                if(j != n-1) res[i][j] = Math.min(res[i][j],res[i][j+1]+1);
            }
        }

        return res;
    }

}
// @lc code=end

