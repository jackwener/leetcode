/*
 * @lc app=leetcode.cn id=1160 lang=rust
 *
 * [1160] 拼写单词
 */

// @lc code=start
impl Solution {
    pub fn count_characters(words: Vec<String>, chars: String) -> i32 {
        let mut res: i32 = 0;
        let mut basket = vec![0; 26];
        
        // Count every char in 'chars' individually
        for c in chars.chars() {
            let index = Solution::calculate_index(c);
            basket[index] = basket[index] + 1;
        }
        
        // Loop through every word
        'outer: for word in words {
            // Clone basket to avoid modifying the original one
            let mut c_basket = basket.clone();
            // Loop through every char in this word
            for (c_index, c) in word.chars().enumerate() {
                let index = Solution::calculate_index(c);
                // if this char still avaliable in 'chars'
                if c_basket[index] > 0 {
                    c_basket[index] = c_basket[index] - 1;
                    // if it reaches the end of the word, count it 
                    if c_index == word.len() - 1 {
                        res = res + word.len() as i32;
                    }
                    // Continue to check next char
                    continue;
                }
                // Current char is not available in 'chars', skip this word
                continue 'outer;
            }
        }
        res
    }
    
    fn calculate_index(c: char) -> usize {
        c as usize - 'a' as usize
    }
}
// @lc code=end

