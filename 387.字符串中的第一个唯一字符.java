import java.util.HashMap;
import java.util.LinkedHashMap;

/*
 * @lc app=leetcode.cn id=387 lang=java
 *
 * [387] 字符串中的第一个唯一字符
 *
 * https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
 *
 * algorithms
 * Easy (41.94%)
 * Likes:    165
 * Dislikes: 0
 * Total Accepted:    54.8K
 * Total Submissions: 129.4K
 * Testcase Example:  '"leetcode"'
 *
 * 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
 * 
 * 案例:
 * 
 * 
 * s = "leetcode"
 * 返回 0.
 * 
 * s = "loveleetcode",
 * 返回 2.
 * 
 * 
 * 
 * 
 * 注意事项：您可以假定该字符串只包含小写字母。
 * 
 */

// @lc code=start
class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character,Integer> map = new HashMap<Character,Integer>();
        int length = s.length();
        for(int i=0;i<length;i++){
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
       }

       for(int i = 0;i<length;i++){
           if(map.get(s.charAt(i))==1){
               return i;
           }
       }
       return -1;
    }
}
// @lc code=end

