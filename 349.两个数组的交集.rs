/*
 * @lc app=leetcode.cn id=349 lang=rust
 *
 * [349] 两个数组的交集
 */

// @lc code=start
use std::collections::HashSet;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut set = HashSet::new();
        let mut result = vec![];
        nums1.into_iter().for_each(|x| {set.insert(x);});
        nums2.into_iter().for_each(|x| {
            if set.contains(&x){
                result.push(x.clone());
                set.remove(&x);
            }
        });
        result
    }
}
// @lc code=end

