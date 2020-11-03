import java.util.Comparator;
import java.util.HashMap;
import java.util.PriorityQueue;

/*
 * @lc app=leetcode.cn id=347 lang=java
 *
 * [347] 前 K 个高频元素
 */

// @lc code=start
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // HashMap<Integer, Integer> map = new HashMap<>();
        // for (int num : nums) {
        //     map.put(num, map.getOrDefault(num, 0) + 1);
        // }

        // PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>(){
        //     @Override
        //     public int compare(Integer o1, Integer o2) {
        //         return map.get(o1) - map.get(o2);
        //     }
        // });

        // for (Integer key : map.keySet()) {
        //     if (pq.size() < k) {
        //         pq.add(key);
        //     } else if (map.get(key) > map.get(pq.peek())) {
        //         pq.remove();
        //         pq.add(key);
        //     }
        // }
        // // 取出最小堆中的元素
        // int[] res = new int[k];
        // for(int i = 0; i < k; i++) {
        //     res[i] = pq.remove();
        // }
        // return res;

        HashMap<Integer, Integer> map = new HashMap<>();
        for(int num: nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer> [] arr = new List[nums.length+1];
        for(Integer num : map.keySet()) {
            int i = map.get(num);
            if(arr[i] == null){
               arr[i] = new ArrayList();
            }
            arr[i].add(num);
        }

        int[] res = new int[k];
        int tmp = 0;
        for(int i = nums.length; i > 0 && tmp < k; i--){
            if (arr[i] == null) continue;
            for(int num: arr[i]) {
                res[tmp] = num;
                tmp += 1;
            }
        }
        return res;
    }
}
// @lc code=end
