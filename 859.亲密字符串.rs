/*
 * @lc app=leetcode.cn id=859 lang=rust
 *
 * [859] 亲密字符串
 */

// @lc code=start
impl Solution {
    pub fn buddy_strings(a: String, b: String) -> bool {
        if a.len() != b.len() { return false }
        if a.len() == 0 { return false } 
                
        if a == b { // if the strings are equal check for duplicate char that can be swapped to maintain equality
            let mut tmpA = a.chars().collect::<Vec<char>>();
            tmpA.sort();
            tmpA.dedup();
            if tmpA.len() < a.len() { return true } // if dedup leads to fewer items in the vec than letters in the string you found a dup char
            return false // if the original strings are equal but there are no duplicate chars, no swap is valid
        }
        
        let mismatches = a.chars().zip(b.chars()).filter(|(a,b)| a != b).collect::<Vec<_>>();
        if mismatches.len() != 2 { return false } // more than 2 mismatches makes it invalid, 1 mismatch also invalid as no potential swap
        mismatches[0].0 == mismatches[1].1 && mismatches[0].1 == mismatches[1].0 // exactly 2 mismatches is only valid if they are complementary       
    }
}

// @lc code=end

