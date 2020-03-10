/*
 * @lc app=leetcode.cn id=350 lang=rust
 *
 * [350] 两个数组的交集 II
 */

// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut map = HashMap::new();
        nums1.iter().for_each(|x| {
            map.entry(x)
            .and_modify(|v| *v += 1)
            .or_insert(1);
        });
    
        nums2.iter().fold(vec![], |mut ret, e| {
            map.entry(e)
            .and_modify(|e2| {
                *e2 -= 1;
                if *e2 >= 0 { ret.push(*e) }
            });
            ret
        })
    }
}
// @lc code=end

