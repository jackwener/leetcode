/*
 * @lc app=leetcode.cn id=257 lang=javascript
 *
 * [257] 二叉树的所有路径
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    if (root === null) return []
    if (root.left === null && root.right === null) return [root.val.toString()]
    let left = binaryTreePaths(root.left)
    let right = binaryTreePaths(root.right)
    let arr = left.concat(right)
    return arr.map(item => root.val.toString() + '->' + item)
}

// @lc code=end

