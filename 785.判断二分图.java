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
    int[] colors ;  // 0未被染色， 1黑  2白
    private int[][] graph;

    public boolean isBipartite(int[][] graph) {
        if (graph == null || graph.length == 0) return false;
        this.graph = graph;
        this.colors = new int[graph.length];
		for(int i = 0; i < graph.length; i++){
            if(colors[i] == 0){
                if(!bfs(i)) return false;
            }
        }
        return true;
    }
    public boolean bfs(int start){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        colors[start] = 1;
        while(!queue.isEmpty()){
            int node = queue.poll();
            for(int i: graph[node]){
                if(colors[i] == colors[node]) return false;
                if(colors[i] == 0) {
                    queue.add(i);
                    colors[i] = colors[node] == 1 ? 2:1;
                }
            }
        }
        return true;
    }
}
// @lc code=end

