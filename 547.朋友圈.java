/*
 * @lc app=leetcode.cn id=547 lang=java
 *
 * [547] 朋友圈
 */

// @lc code=start
class Solution {
    int[] father;
    public int findCircleNum(int[][] M) {
        father = new int[M.length];
        for (int i = 0; i < father.length; i++) {
            father[i] = i;
        }
        
        for(int i = 0; i < M.length; i++){
            for (int j = 0; j < M.length; j++) {
                if(M[i][j] == 1 && i != j){
                    union(i, j);
                }
            }
        }
        int count = 0;
        for (int i = 0; i < father.length; i++) {
            if (father[i] == i)
                count++;
        }
        return count;
    }

    public void union(int x, int y){
        int a = find(x);
        int b = find(y);
        if(a != b){
            father[a] = b;
        }
    }

    public int find(int son) {
        // if (son != father[son]) {
        //     father[son] = find(father[son]);
        // }
        // return father[son];
        
        // 不用递归，小优化
        int root=son,temp;
        while(root!=father[root])
        root=father[root];
        while(son!=father[son])
        {
            temp=father[son];
            father[son]=root;
            son=temp;
        }
        return root;
    }
}

// @lc code=end

