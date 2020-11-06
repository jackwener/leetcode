/*
 * @lc app=leetcode.cn id=1122 lang=java
 *
 * [1122] 数组的相对排序
 */

// @lc code=start
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] bucket = new int [1001];
        int[] res = new int [arr1.length];
        int j = 0;
        for(int num : arr1) {
            bucket[num] += 1;
        }
        for(int num : arr2) {
            while(bucket[num] > 0){
                res[j] = num;
                bucket[num]--;
                j++;
            }
        }
        for(int i = 0; i <= 1000; i++){
            while(bucket[i] > 0){
                res[j] = i;
                bucket[i]--;
                j++;
            }
        }
        return res;
    }
}
// @lc code=end

