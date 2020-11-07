/*
 * @lc app=leetcode.cn id=814 lang=java
 *
 * [814] 二叉树剪枝
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode pruneTree(TreeNode root) {
        boolean result = helper(root);
        return result == true? root: null;
    }

    public boolean helper(TreeNode root) {
        if(root == null) return false;

        if(helper(root.left) == false) {
            root.left = null;
        }
        if(helper(root.right) == false) {
            root.right = null;
        }

        return root.val == 1 || helper(root.left) || helper(root.right);
    }
}
// @lc code=end

