/*
 * @lc app=leetcode.cn id=886 lang=java
 *
 * [886] 可能的二分法
 */

// @lc code=start
class Solution {
    int N;  //共多少人
    int[] father;   //并查集
    public boolean possibleBipartition(int _N, int[][] dl) {
        N = _N+1;   
        father = new int[N*2+5];    //开两倍的数组
        for(int i = 1; i < N*2+5; i++) //初始化并查集
            father[i] = i;
        for(int i = 0; i < dl.length; i++){
            int x = find(dl[i][0]); //查找自己的根节点
            int y = find(dl[i][1]);
            int a = find(dl[i][0] + N); //查找自己不喜欢的人的根节点
            int b = find(dl[i][1] + N); 
            if(x == y) return false; //发现这俩人已经在一组
            else{
                father[a] = y;  //将不喜欢的人合并
                father[b] = x;
            }
        }
        return true;
    }
    private int find(int x){ //寻找根节点
        if(x != father[x])  
            father[x] = find(father[x]); //路径压缩
        return father[x];
    }
}
// @lc code=end

