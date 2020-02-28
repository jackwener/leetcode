
/*
 * @lc app=leetcode.cn id=1002 lang=java
 *
 * [1002] 查找常用字符
 */

// @lc code=start
class Solution {
    public List<String> commonChars(String[] A) {
        int[] counter = new int[26];
        for(char c : A[0].toCharArray())  // 统计第1个单词各个字母的词频
            counter[c - 'a']++;
        
        for (int i = 1; i < A.length; i++) {
            int[] tempArr = new int[26];
            for (char c : A[i].toCharArray()) {
                tempArr[c - 'a']++;      // 后一个单词的字母词频
            }
            for (int j = 0; j < 26; j++) {
                if(tempArr[j] < counter[j])
                    counter[j] = tempArr[j];  // 字母频次的交集
            }
        }
    
        LinkedList<String> resList = new LinkedList<>();
        for (int i = 0; i < 26; i++) {
            while (counter[i]-- > 0) {  // counter[0] 记录字母a的出现次数
                resList.addLast("" + (char)('a' + i));
            }
        }
        return resList;
    }
}
// @lc code=end

