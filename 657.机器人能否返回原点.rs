/*
 * @lc app=leetcode.cn id=657 lang=rust
 *
 * [657] 机器人能否返回原点
 */

// @lc code=start
impl Solution {
    pub fn judge_circle(moves: String) -> bool {
        let mut x: i32 = 0;
        let mut y: i32 = 0;
        moves.chars().for_each(|c| {
            match c {
                'U' => y += 1,
                'D' => y -= 1,
                'L' => x -= 1,
                'R' => x += 1,
                _ => println!("error"),
            }
        });
        x == 0 && y == 0
    }
}
// @lc code=end

