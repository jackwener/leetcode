/*
 * @lc app=leetcode.cn id=766 lang=java
 *
 * [766] 托普利茨矩阵
 */

// @lc code=start
class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        int rowNum = matrix.length;
        int colNum = matrix[0].length;
        int len = rowNum + colNum - 1;
        int[] startNums = new int[len];

        for(int i = 0; i < len; i ++) {
            if(i < rowNum){
                startNums[i] = matrix[rowNum-1 - i][0];
            } else {
                startNums[i] = matrix[0][i - (rowNum-1)];
            }
        }

        for(int i = 0; i < rowNum; i++){
            int startIndex = -1 * (i - (rowNum - 1));
            for(int j = 0; j < colNum; j++) {
                if(matrix[i][j] != startNums[startIndex+j]){
                    return false;
                }
            }
        }

        return true;
    }
}
// @lc code=end

