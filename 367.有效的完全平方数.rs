/*
 * @lc app=leetcode.cn id=367 lang=rust
 *
 * [367] 有效的完全平方数
 */

// @lc code=start
impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        if num == 1 { return true;}

        let num = num as i64;
        let mut x: i64 = num / 2;
        while x.pow(2) > num {
            x = (x + num / x) / 2;
        }
        println!("this is {}",x);
        return x*x == num;
    }
}
// @lc code=end

