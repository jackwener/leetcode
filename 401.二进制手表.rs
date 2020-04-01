/*
 * @lc app=leetcode.cn id=401 lang=rust
 *
 * [401] 二进制手表
 */

// @lc code=start
use std::cmp::{max, min};
use std::collections::HashMap;

impl Solution {
    pub fn read_binary_watch(num: i32) -> Vec<String> {
        let mut inverted_map = HashMap::new();
        for i in 0i32..60i32 {
            let bit_count = i.count_ones() as i32;
            inverted_map.entry(bit_count).or_insert(vec![]).push(i);
        }
        
        let mut result = vec![];
        // there are at most 3 digits for hour and 5 digits for minutes
        for i in max(0, num - 5)..=min(num, 3) {
            for hour in inverted_map[&i].iter().take_while(|&&h| h < 12) {
                for minute in inverted_map[&(num - i)].iter() {
                    result.push(format!("{}:{:02}", hour, minute));
                }
            }

        }
        result
    }
}
// @lc code=end

