/*
 * @lc app=leetcode.cn id=684 lang=java
 *
 * [684] 冗余连接
 */

// @lc code=start
class Solution {
    private int[] res=new int[2];
    public int[] findRedundantConnection(int[][] edges) {
        int[] father = new int[edges.length+1];

        for(int i = 1;i < father.length; i++)father[i]=i;

        for(int i = 0;i < edges.length; i++){
            union(edges[i][0], edges[i][1], father);//两个节点之间结合
        }
        return res;
    }
    
    public void union(int x, int y, int[] father){
        int fx = find(x, father);
        int fy = find(y, father);
        if(fx == fy){
            res[0] = x;
            res[1] = y;
        }
        father[fx] = fy;
    }

    public int find(int x,int[] father){
        if(x != father[x]) return find(father[x], father);
        return father[x];
    }
}

// @lc code=end

