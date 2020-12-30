/*
 * @lc app=leetcode.cn id=1046 lang=java
 *
 * [1046] 最后一块石头的重量
 */

// @lc code=start
class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for(int stone: stones) {
            pq.offer(stone);
        }

        while(pq.size()>=2){
            int a = pq.poll();
            int b = pq.poll();
            if(a > b) {
                pq.offer(a-b);
            }
        }

        return pq.isEmpty()?0: pq.poll();
    }
}
// @lc code=end

