import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=560 lang=java
 *
 * [560] 和为K的子数组
 */

// @lc code=start
class Solution {
    public int subarraySum(int[] nums, int k) {
        int sum = 0;
        int res = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            if(k != 0) sum %= k;
            if(sum == 0) res ++;
            if(map.containsKey(sum)){
                res ++;
            } else {
                map.put(sum, i);
            }
        }
        return res;
    }
}
// @lc code=end

