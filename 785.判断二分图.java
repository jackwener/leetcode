import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

/*
 * @lc app=leetcode.cn id=785 lang=java
 *
 * [785] 判断二分图
 */

// @lc code=start
class Solution {
    // int[] colors ;  // 0未被染色， 1黑  2白
    // private int[][] graph;

    // public boolean isBipartite(int[][] graph) {
    //     if (graph == null || graph.length == 0) return false;
    //     this.graph = graph;
    //     this.colors = new int[graph.length];
	// 	for(int i = 0; i < graph.length; i++){
    //         if(colors[i] == 0){
    //             if(!bfs(i)) return false;
    //         }
    //     }
    //     return true;
    // }
    // public boolean bfs(int start){
    //     Queue<Integer> queue = new LinkedList<>();
    //     queue.add(start);
    //     colors[start] = 1;
    //     while(!queue.isEmpty()){
    //         int node = queue.poll();
    //         for(int i: graph[node]){
    //             if(colors[i] == colors[node]) return false;
    //             if(colors[i] == 0) {
    //                 queue.add(i);
    //                 colors[i] = colors[node] == 1 ? 2:1;
    //             }
    //         }
    //     }
    //     return true;
    // }

    int[] father;   //并查集
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        father = new int[n*2];    //开两倍的数组
        for(int i = 0; i < n*2; i++) //初始化并查集
            father[i] = i;
        for(int i = 0; i < graph.length; i++){
            for(int j = 0; j < graph[i].length; j++){
                int x = find(i); //查找自己的根节点
                int y = find(graph[i][j]);
                int a = find(i + n); //查找自己不喜欢的人的根节点
                int b = find(graph[i][j] + n); 
                if(x == y) return false; //发现这俩人已经在一组
                else{
                    father[a] = y;  //将不喜欢的人合并
                    father[b] = x;
                }
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

