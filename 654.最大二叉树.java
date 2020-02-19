import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=654 lang=java
 *
 * [654] 最大二叉树
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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if(nums==null||nums.length==0){
            return null;
        }
        return constructMaximumBinaryTree(nums,0,nums.length-1);
    }
    public TreeNode constructMaximumBinaryTree(int[]nums,int start,int end){
        if(start>end){
            return null;
        }
        int maxValueIndex=findMaxValueIndex(nums,start,end);
        TreeNode root=new TreeNode(nums[maxValueIndex]);
        root.left=constructMaximumBinaryTree(nums,start,maxValueIndex-1);
        root.right=constructMaximumBinaryTree(nums,maxValueIndex+1,end);
        return root;
    }
    public int findMaxValueIndex(int[] nums,int start,int end){  //此函数用于找出数组中最大值的下标
        int maxValue=Integer.MIN_VALUE;
        int maxValueIndex=start;
        for(int i=start;i<=end;++i){
            if(nums[i]>maxValue){
                maxValue=nums[i];
                maxValueIndex=i;
            }
        }
        return maxValueIndex;
    }
}


// @lc code=end

