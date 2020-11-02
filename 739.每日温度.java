/*
 * @lc app=leetcode.cn id=739 lang=java
 *
 * [739] 每日温度
 */

// @lc code=start
class Solution {
    public int[] dailyTemperatures(int[] T) {
        Stack<Pair<Integer, Integer>> stack = new Stack<>();
        int[] res = new int[T.length];
        for(int i = 0; i < T.length; i++) {
            while(!stack.empty() && T[i] > stack.peek().getValue()) {
                int j = stack.pop().getKey();
                res[j] = i - j;
            }
            Pair<Integer, Integer> pair = new Pair<>(i, T[i]);
            stack.push(pair);
        }
        return res;
    }
}
// @lc code=end

