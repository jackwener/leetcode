/*
 * @lc app=leetcode.cn id=538 lang=java
 *
 * [538] 把二叉搜索树转换为累加树
 *
 * https://leetcode-cn.com/problems/convert-bst-to-greater-tree/description/
 *
 * algorithms
 * Easy (57.56%)
 * Likes:    181
 * Dislikes: 0
 * Total Accepted:    13.2K
 * Total Submissions: 22.9K
 * Testcase Example:  '[5,2,13]'
 *
 * 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater
 * Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
 * 
 * 例如：
 * 
 * 
 * 输入: 二叉搜索树:
 * ⁠             5
 * ⁠           /   \
 * ⁠          2     13
 * 
 * 输出: 转换为累加树:
 * ⁠            18
 * ⁠           /   \
 * ⁠         20     13
 * 
 * 
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
    // public TreeNode convertBST(TreeNode root) {
    //     Stack<TreeNode> stack = new Stack<>();
    //     TreeNode cur = root;
    //     while(cur != null) {
    //         stack.push(cur);
    //         cur = cur.right;
    //     }

    //     int sumTmp = 0;
    //     while(!stack.empty()) {
    //         cur = stack.pop();
    //         sumTmp += cur.val;
    //         cur.val = sumTmp;

    //         cur = cur.left;
    //         while(cur != null) {
    //             stack.push(cur);
    //             cur = cur.right;
    //         }
    //     }

    //     return root;
    // }
    public TreeNode convertBST(TreeNode root) {
        after(root, 0);
        return root;
    }

    public int after(TreeNode node, Integer parent) {
        if (node == null) return parent;
        int right = after(node.right, parent);
        node.val = node.val + right;
        return after(node.left, node.val);
    }
}
// @lc code=end

