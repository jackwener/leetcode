import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=589 lang=java
 *
 * [589] N叉树的前序遍历
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
    public List<Integer> preorder(Node root) {
        List<Integer> list = new ArrayList<Integer>();
        helper(root, list);
        return list;
    }
    public void helper(Node root, List<Integer> list){
        if(root == null) return;
        list.add(root.val);
        for (int i = 0; i <root.children.size() ; i++) {
            helper(root.children.get(i),list);
        }
    }
}
// @lc code=end

