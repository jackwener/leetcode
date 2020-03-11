/*
 * @lc app=leetcode.cn id=1200 lang=rust
 *
 * [1200] 最小绝对差
 */

// @lc code=start
impl Solution {
    pub fn minimum_abs_difference(mut arr: Vec<i32>) -> Vec<Vec<i32>> {
        use std::cmp;
        arr.sort();
        let min = arr[..].windows(2).fold(i32::max_value(), |min, slice| {
            cmp::min(slice[1] - slice[0], min)
        });
        arr.windows(2)
            .filter_map(|slice| {
                if slice[1] - slice[0] == min {
                    Some(vec![slice[0], slice[1]])
                } else {
                    None
                }
            })
            .collect::<Vec<Vec<_>>>()
    }
}
// @lc code=end

