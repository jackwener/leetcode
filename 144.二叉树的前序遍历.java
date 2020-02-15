import java.util.ArrayList;
import java.util.Stack;

import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=144 lang=java
 *
 * [144] 二叉树的前序遍历
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// class Solution {
//     public List<Integer> preorderTraversal(TreeNode root) {
//         List<Integer> res = new ArrayList<>();
//         helper(root, res);
//         return res;
//     }

//     public void helper(TreeNode root, List<Integer> res) {
//         if(root == null) return;
//         res.add(root.val);
//         helper(root.left, res);
//         helper(root.right, res);
//     }
// }
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        List<Integer> res = new ArrayList<>();
        if(root == null) return res;
        // while (p != null || !stack.isEmpty()) {
        //     while (p != null) {
        //         res.add(p.val);
        //         stack.push(p);
        //         p = p.left;
        //     }
        //     p = stack.pop().right;
        // }
        // return res;
        while(!stack.isEmpty()){
            TreeNode node = stack.pop();
            res.add(node.val);
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
        }
        return res;
    }
}
// @lc code=end

