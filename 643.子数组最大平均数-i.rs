/*
 * @lc app=leetcode.cn id=643 lang=rust
 *
 * [643] 子数组最大平均数 I
 */

// @lc code=start
impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let avr: Vec<f64> = nums.into_iter().map(|x| x as f64 / k as f64).collect();
        let mut max = avr.clone()[0..k as usize]
            .into_iter()
            .fold(0., |a, &b| a + b);
        let mut sum = max;
        for i in k as usize..avr.len() {
            sum = sum - avr[i - k as usize] + avr[i];
            if sum > max {
                max = sum;
            }
        }
        max
    }
}
// @lc code=end

