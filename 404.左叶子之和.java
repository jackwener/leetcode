/*
 * @lc app=leetcode.cn id=404 lang=java
 *
 * [404] 左叶子之和
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
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return helper(root, false);
    }

    public int helper(TreeNode root, boolean flag){
        if(root == null) return 0;
        // 如果节点是左叶子
        if(flag && root.right == null && root.left == null){
            return root.val;
        }
        return helper(root.left, true) + helper(root.right, false);
    }
}
// @lc code=end

