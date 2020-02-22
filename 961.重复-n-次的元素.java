import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=961 lang=java
 *
 * [961] 重复 N 次的元素
 */

// @lc code=start
class Solution {
    public int repeatedNTimes(int[] A) {
        // HashMap<Integer,Integer> map = new HashMap<>();
        // for(int num : A){
        //     map.put(num, map.getOrDefault(num, 0) + 1);
        // }
        // for(int k: map.keySet())
        //     if(map.get(k) > 1) return k;
        // return 0;

        for (int k = 1; k <= 3; ++k)
            for (int i = 0; i < A.length - k; ++i)
                if (A[i] == A[i+k])
                    return A[i];

        return 0;
    }
}
// @lc code=end

