/*
 * @lc app=leetcode.cn id=222 lang=java
 *
 * [222] 完全二叉树的节点个数
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
    public int count = 0;
    public int countNodes(TreeNode root) {
        if(root == null) return 0;
        count += 1;
        countNodes(root.left);
        countNodes(root.right);
        return count;
    }
}
// @lc code=end

