import javax.swing.tree.TreeNode;

/*
 * @lc app=leetcode.cn id=513 lang=java
 *
 * [513] 找树左下角的值
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
    private int ans = -1;
    //记录当前最大高度
    private int max = -1;

    public int findBottomLeftValue(TreeNode root) {
        dfs(root, 0);
        return ans;
    }

    private void dfs(TreeNode root, int h) {
        if(root == null) {
            return;
        }
        if(root.left == null && root.right == null) {
            if(h > max) {
                max = h;
                ans = root.val;
            }
        }
        dfs(root.left, h + 1);
        dfs(root.right, h + 1);
    }
}
// @lc code=end

