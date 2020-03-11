/*
 * @lc app=leetcode.cn id=633 lang=rust
 *
 * [633] 平方数之和
 */

// @lc code=start
impl Solution {
    pub fn judge_square_sum(c: i32) -> bool {
        // for (int i = 2; i * i <= c; i++) {
        //     int count = 0;
        //     if (c % i == 0) {
        //         while (c % i == 0) {
        //             count++;
        //             c /= i;
        //         }
        //         if (i % 4 == 3 && count % 2 != 0)
        //             return false;
        //     }
        // }
        // return c % 4 != 3;

        let mut c = c;
        let mut i = 2;
        while i <= c {
            let mut count = 0;
            if (c % i == 0) {
                while (c % i == 0) {
                    count += 1;
                    c /= i;
                }
                if (i % 4 == 3 && count % 2 != 0){
                    return false;
                }
            }
            i += 1;
        }
        c % 4 != 3
    }
}
// @lc code=end

