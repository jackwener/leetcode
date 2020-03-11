/*
 * @lc app=leetcode.cn id=389 lang=rust
 *
 * [389] 找不同
 */

// @lc code=start
impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        // let mut letters = vec![0; 26];
        // s.chars().for_each(|c| {
        //     let idx = c as i32 - 'a' as i32 + 1;
        //     letters[idx] += 1;
        // });
        // s.chars().for_each(|c| {
        //     let idx = c as u32 - 'a' as u32 + 1;
        //     letters[idx] -= 1;
        // });
        
        let sum_s: u8 = s.chars().map(|c| c as u8).sum();
        let sum_t: u8 = t.chars().map(|c| c as u8).sum();
        char::from(sum_t - sum_s)
       
    }
}
// @lc code=end

