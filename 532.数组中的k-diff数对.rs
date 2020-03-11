/*
 * @lc app=leetcode.cn id=532 lang=rust
 *
 * [532] 数组中的K-diff数对
 */

// @lc code=start
use std::collections::HashSet;
impl Solution {
    pub fn find_pairs(nums: Vec<i32>, k: i32) -> i32 {
        // let mut tally = HashMap::with_capacity(nums.len());
        // for num in nums.iter() {
        //     *tally.entry(num).or_insert(0) += 1;
        // }
        // match k {
        //     k if k < 0 => 0,
        //     k if k == 0 => tally.iter().filter(|(_,val)| **val > 1).count() as i32,
        //     _ => tally.iter().filter(|(x, _)| nums.contains(&(**x-k))).count() as i32
        // }

        if k<0 {return 0;}
        let mut saw = HashSet::new();
        let mut diff = HashSet::new();
        nums.iter().for_each(|num| {
            if saw.contains(&(num-k)){diff.insert(num-k);}
            if saw.contains(&(num+k)){diff.insert(*num);}
            saw.insert(*num);
        });
        diff.len() as i32
    }
}
// @lc code=end

