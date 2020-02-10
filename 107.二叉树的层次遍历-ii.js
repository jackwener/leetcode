/*
 * @lc app=leetcode.cn id=107 lang=javascript
 *
 * [107] 二叉树的层次遍历 II
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
 * @return {number[][]}
 */
var levelOrderBottom = function(root) {
    let result = []
    let level = 0
    let traverse = function(node, level){
        if(node === null) return
        if(!result[level]) result[level] = []
        result[level].push(node.val)
        traverse(node.left,level+1)
        traverse(node.right,level+1)
    }

    traverse(root,0)
    return result.reverse()
  }
// @lc code=end

