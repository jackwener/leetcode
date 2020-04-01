/*
 * @lc app=leetcode.cn id=7 lang=rust
 *
 * [7] 整数反转
 */

// @lc code=start
impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut res = 0;
        let mut sign = 1;
        if x < 0{
            sign = -1;
        }
        let mut x = x.abs();
        while x > 0 {
            let new = res * 10 + x % 10;
			// check whether it is overflow
            if (new - x % 10) / 10 != res { 
                return 0; 
            }
            res = new;
            x = x / 10;     
        }
        return res * sign;
    }
}
// @lc code=end

