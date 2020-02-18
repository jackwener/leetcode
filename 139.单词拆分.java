/*
 * @lc app=leetcode.cn id=139 lang=java
 *
 * [139] 单词拆分
 */

// @lc code=start
// class Solution {

//     public class TrieNode {       
//         boolean flag;  
//         HashMap<Character, TrieNode> next = new HashMap<Character, TrieNode>(); 
          
//         public TrieNode() {  
//             flag = false; 
//         }  
//     }

//     TrieNode root;
//     //List<Integer>  memo = new LinkedList<Integer>();
//     int[] memo;

//     public boolean helper(String s, int start, int end) {
//         if(start == end) return true;
//         if (memo[start] != 0)
//             return memo[start] > 0;
//         TrieNode node = root;
//         for (int i = start; i < end; ++i) {
//             if (!node.next.containsKey(s.charAt(i)))
//                 break;
//             node = node.next.get(s.charAt(i));
//             if (node.flag){
//                 if(helper(s, i + 1, end)){
//                     memo[start] = 1;
//                     return true;
//                 }
//             }
//         }
//         memo[start] = -1;
//         return false;
//     }

//     public boolean wordBreak(String s, List<String> wordDict) {
//         memo = new int[s.length()];
//         root = new TrieNode();
//         TrieNode node = root;
//         for(String word : wordDict){
//             node = root;
//             for(char ch : word.toCharArray()){
//                 if(!node.next.containsKey(ch)){
//                     node.next.put(ch, new TrieNode());
//                 }
//                 node = node.next.get(ch);
//             }
//             node.flag = true;
//         }
//         return helper(s, 0, s.length());
//     }
// }


// public class Solution {
//     public boolean wordBreak(String s, List<String> wordDict) {
//         Set<String> wordDictSet=new HashSet(wordDict);
//         Queue<Integer> queue = new LinkedList<>();
//         int[] visited = new int[s.length()];
//         queue.add(0);
//         while (!queue.isEmpty()) {
//             int start = queue.remove();
//             if (visited[start] == 0) {
//                 for (int end = start + 1; end <= s.length(); end++) {
//                     if (wordDictSet.contains(s.substring(start, end))) {
//                         queue.add(end);
//                         if (end == s.length()) {
//                             return true;
//                         }
//                     }
//                 }
//                 visited[start] = 1;
//             }
//         }
//         return false;
//     }
// }

public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordDictSet=new HashSet(wordDict);
        boolean[] dp = new boolean[s.length() + 1];
        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordDictSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }
}


// @lc code=end

