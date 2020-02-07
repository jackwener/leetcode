import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/*
 * @lc app=leetcode.cn id=217 lang=java
 *
 * [217] 存在重复元素
 */

// @lc code=start
class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Map<Integer, Integer> map = new HashMap<>(nums.length);
        // for(int num: nums){
        //     if(map.containsKey(num)){
        //         return true;
        //     } else {
        //         map.put(num, num);
        //     }
        // }
        // return false;
        Set<Integer> set = new HashSet<>(nums.length);
        for(int num : nums){
            set.add(num);
        }
        return set.size() != nums.length;
    }
}
// @lc code=end

