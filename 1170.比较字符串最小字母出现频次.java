/*
 * @lc app=leetcode.cn id=1170 lang=java
 *
 * [1170] 比较字符串最小字母出现频次
 */

// @lc code=start
class Solution {
    public int[] numSmallerByFrequency(String[] queries, String[] words) {
        int[] res = new int[queries.length];
        
        int[] count = new int[12];
        for(String word : words) {
            count[f(word)] += 1;
        }
        for(int i = 9; i >= 0; i--) {
            count[i] += count[i+1];
        }
        for(int i = 0; i < queries.length; i++){
            res[i] = count[f(queries[i]) + 1];
        }

        return res;
    }

    public int f(String s) {
        char c = s.charAt(0);
        int count = 0;
        for (char tmp : s.toCharArray()){
            if (tmp == c)
                count++;
            else if (tmp < c){
                c = tmp;
                count = 1;
            }
        }
        return count;
    }
}
// @lc code=end

