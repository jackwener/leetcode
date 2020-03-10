/*
 * @lc app=leetcode.cn id=383 lang=rust
 *
 * [383] 赎金信
 */

// @lc code=start
use std::collections::HashSet;
impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        use std::collections::HashMap;
        let mut letters = HashMap::new();
        
        magazine.chars().for_each(|x| {
            letters.entry(x)
            .and_modify(|e| { *e += 1 })
            .or_insert(1);
        });


        for c in ransom_note.chars() {
            if let Some(count) = letters.get_mut(&c) {
                *count -= 1;
                if *count < 0 {
                    return false;
                }
            } else {
                return false;
            }
        }
        true
        
        // ransom_note.chars().for_each(|x| {
        //     if let Some(count) = letters.get_mut(&x) {
        //         *count -= 1;
        //         if *count < 0 {
        //             return false;
        //         }
        //     } else {
        //         return false;
        //     }
        // });
        //true
    }
}
// @lc code=end

