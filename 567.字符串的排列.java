import java.util.Arrays;
import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=567 lang=java
 *
 * [567] 字符串的排列
 */

// @lc code=start
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s2.length() < s1.length()) return false;

        int[] needs = new int[26];
        int[] res = new int[26];
        for(int i = 0; i < s1.length(); i++){
            needs[s1.charAt(i) - 'a'] += 1;
            res[s2.charAt(i) - 'a'] += 1;
        }

        for(int i = s1.length(); i < s2.length(); i++){
            if(Arrays.equals(res, needs)){
                return true;
            }
            res[s2.charAt(i) - 'a'] += 1;
            res[s2.charAt(i-s1.length()) - 'a'] -= 1;
        }
        return Arrays.equals(res, needs);
    }
}
// @lc code=end

