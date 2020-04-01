/*
 * @lc app=leetcode.cn id=441 lang=rust
 *
 * [441] 排列硬币
 */

// @lc code=start
impl Solution {
    pub fn arrange_coins(n: i32) -> i32 {
        ((((1 + 8 * n as i64) as f64).sqrt() - 1f64) / 2f64) as i32
    }
}
// @lc code=end

