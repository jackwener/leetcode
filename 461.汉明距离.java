/*
 * @lc app=leetcode.cn id=461 lang=java
 *
 * [461] 汉明距离
 */

// @lc code=start
class Solution {
    public int hammingDistance(int x, int y) {
        int xor = x ^ y;
        // return Integer.bitCount(xor);

        // int count = 0;
        // while(xor != 0) {
        //     count += 1;
        //     xor = xor & (xor - 1);
        // }
        // return count;


        xor = (xor &0x55555555) + ((xor >>1) &0x55555555) ; 
        xor = (xor &0x33333333) + ((xor >>2) &0x33333333) ; 
        xor = (xor &0x0f0f0f0f) + ((xor >>4) &0x0f0f0f0f) ; 
        xor = (xor &0x00ff00ff) + ((xor >>8) &0x00ff00ff) ; 
        xor = (xor &0x0000ffff) + ((xor >>16) &0x0000ffff) ; 

        return xor;
    }
}
// @lc code=end

