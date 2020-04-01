/*
 * @lc app=leetcode.cn id=504 lang=rust
 *
 * [504] 七进制数
 */

// @lc code=start
impl Solution {
    pub fn convert_to_base7(mut num: i32) -> String {
        if num == 0 {
            return "0".to_string();
        }
        let mut s = String::new();
        let sign = if num < 0 {
            num *= -1;
            "-".to_string()
        } else {
            "".to_string()
        };
        while num > 0 {
            s = (num % 7).to_string() + &s;
            num /= 7;
        }
        sign + &s
    }
}
// @lc code=end

