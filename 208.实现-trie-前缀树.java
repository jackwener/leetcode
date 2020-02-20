import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=208 lang=java
 *
 * [208] 实现 Trie (前缀树)
 */

// @lc code=start
class Trie {

    public class TrieNode {       
        boolean flag;  
        HashMap<Character, TrieNode> next = new HashMap<Character, TrieNode>(); 
          
        public TrieNode() {  
            flag = false; 
        }  
    }

    TrieNode root;

    Trie(){
        this.root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode node = root;
        for(Character c : word.toCharArray()){
            if(!node.next.containsKey(c)) {
                TrieNode newNode = new TrieNode();
                node.next.put(c, newNode);
                node = newNode;
            } else{
                node = node.next.get(c);
            }
       }
       node.flag = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        if(word.length() == 0) return true;
        TrieNode node = root;
        for(Character c : word.toCharArray()){
            if(!node.next.containsKey(c)) return false;
            node = node.next.get(c);
        }
        return node.flag;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        if(prefix.length() == 0) return true;
        TrieNode node = root;
        for(Character c : prefix.toCharArray()){
            if(!node.next.containsKey(c)) return false;
            node = node.next.get(c);
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
// @lc code=end

