/*
 * @lc app=leetcode.cn id=475 lang=rust
 *
 * [475] 供暖器
 */

// @lc code=start
impl Solution {
    pub fn find_radius(houses: Vec<i32>, heaters: Vec<i32>) -> i32 {
        let heaters = &mut { heaters };
        heaters.sort();
        let mut radius = 0;
        for house in houses {
            let min_house_heater_dist = match heaters.binary_search(&house) {
                Ok(_) => 0,
                Err(i) => {
                    if i == 0 {
                        heaters[i] - house
                    } else if i == heaters.len() {
                        house - heaters[i - 1]
                    } else {
                        std::cmp::min(heaters[i] - house, house - heaters[i - 1])
                    }
                }
            };
            radius = std::cmp::max(radius, min_house_heater_dist);
        }
        radius
    }
}
// @lc code=end

