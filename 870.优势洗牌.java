/*
 * @lc app=leetcode.cn id=870 lang=java
 *
 * [870] 优势洗牌
 */

// @lc code=start
class Solution {
    public int[] advantageCount(int[] A, int[] B) {
        Pair<Integer, Integer>[] BPair = new Pair[B.length];
        for(int i = 0; i < B.length; i++) {
            BPair[i] = new Pair(i, B[i]);
        }
        int[] Ac = A.clone();
        Arrays.sort(Ac);
        Arrays.sort(BPair, (a,b) -> a.getValue() - b.getValue());

        int[] res = new int[A.length];

        int i = 0, j = 0;
        while(i < A.length) {
            if(Ac[i] > BPair[j].getValue()){
                res[BPair[j].getKey()] = Ac[i];
                i++;
                j++;
            } else {
                res[BPair[A.length - 1 - (i-j)].getKey()] = Ac[i];
                i++;
            }
        }
        return res;
    }
}
// @lc code=end

