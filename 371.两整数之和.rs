/*
 * @lc app=leetcode.cn id=371 lang=rust
 *
 * [371] 两整数之和
 */

// @lc code=start
impl Solution {
    pub fn get_sum(a: i32, b: i32) -> i32 {
        //let mut temp_sum :i32 = a ^ b;
        //let mut carry = (a & b) << 1;
        let mut a = a;
        let mut b = b;
        while b != 0 {
            let mut tmp: i32 = a;
            a = a ^ b;
            b = (tmp & b) << 1;
        }
        a
    }
}
// @lc code=end

