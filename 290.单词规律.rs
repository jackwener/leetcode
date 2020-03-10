/*
 * @lc app=leetcode.cn id=290 lang=rust
 *
 * [290] 单词规律
 */

// @lc code=start
impl Solution {
    pub fn word_pattern(pattern: String, str: String) -> bool {
        use std::collections::HashSet;
        if pattern.len() != str.split_whitespace().count() {
            return false
        }
        
        const ASCII_LOWERCASE_BASE : usize = 'a' as usize;

        let mut map: [Option<String>; 26] = Default::default();
        let mut used_words = HashSet::new();

        for (ch, word) in pattern.chars().zip(str.split_whitespace()){
            let idx = ch as usize - ASCII_LOWERCASE_BASE;

            match &map[idx] {
                Some(val) if val != word => {
                    return false;
                },
                None if used_words.contains(word) =>{
                    return false;
                }
                None =>{
                    map[idx] = Some(String::from(word));
                    used_words.insert(word);
                },
                _ => {}
            }
        }
        true
    }
}
// @lc code=end

