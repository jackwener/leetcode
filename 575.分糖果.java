import java.util.HashMap;
import java.util.HashSet;

/*
 * @lc app=leetcode.cn id=575 lang=java
 *
 * [575] 分糖果
 */

// @lc code=start
class Solution {
    public int distributeCandies(int[] candies) {
        HashSet<Integer> set = new HashSet<>();
        for(int num : candies) {
            set.add(num);
        }
        return Math.min(set.size(), candies.length / 2);
    }
}
// @lc code=end

