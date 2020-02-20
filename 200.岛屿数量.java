/*
 * @lc app=leetcode.cn id=200 lang=java
 *
 * [200] 岛屿数量
 */

// @lc code=start
/**
 * 方法一：深度优先遍历
 */
// class Solution {
//     void dfs(char[][] grid, int r, int c) {
//       int row = grid.length;
//       int column = grid[0].length;
  
//       if (r < 0 || c < 0 || r >= row || c >= column || grid[r][c] == '0') {
//         return;
//       }
  
//       grid[r][c] = '0';
//       dfs(grid, r - 1, c);
//       dfs(grid, r + 1, c);
//       dfs(grid, r, c - 1);
//       dfs(grid, r, c + 1);
//     }
  
//     public int numIslands(char[][] grid) {
//       if (grid == null || grid.length == 0) {
//         return 0;
//       }
  
//       int row = grid.length;
//       int column = grid[0].length;
//       int island_nums = 0;
//       for(int i = 0; i < row; i ++){
//           for(int j = 0; j < column; j ++){
//             if(grid[i][j] == '1'){
//                 ++ island_nums;
//                 dfs(grid, i, j);
//             }
//           }
//       }

//       return island_nums;
//     }
//   }

class Solution {
    class UnionFind {
      int count; // # of connected components
      int[] parent;
      int[] rank;
  
      public UnionFind(char[][] grid) { // for problem 200
        count = 0;
        int m = grid.length;
        int n = grid[0].length;
        parent = new int[m * n];
        rank = new int[m * n];
        for (int i = 0; i < m; ++i) {
          for (int j = 0; j < n; ++j) {
            if (grid[i][j] == '1') {
              parent[i * n + j] = i * n + j;
              ++count;
            }
            rank[i * n + j] = 0;
          }
        }
      }
  
      public int find(int i) { // path compression
        if (parent[i] != i) parent[i] = find(parent[i]);
        return parent[i];
      }
  
      public void union(int x, int y) { // union with rank
        int rootx = find(x);
        int rooty = find(y);
        if (rootx != rooty) {
          if (rank[rootx] > rank[rooty]) {
            parent[rooty] = rootx;
          } else if (rank[rootx] < rank[rooty]) {
            parent[rootx] = rooty;
          } else {
            parent[rooty] = rootx; rank[rootx] += 1;
          }
          --count;
        }
      }
  
      public int getCount() {
        return count;
      }
    }
  
    public int numIslands(char[][] grid) {
      if (grid == null || grid.length == 0) {
        return 0;
      }
  
      int nr = grid.length;
      int nc = grid[0].length;
      int num_islands = 0;
      UnionFind uf = new UnionFind(grid);
      for (int r = 0; r < nr; ++r) {
        for (int c = 0; c < nc; ++c) {
          if (grid[r][c] == '1') {
            grid[r][c] = '0';
            if (r - 1 >= 0 && grid[r-1][c] == '1') {
              uf.union(r * nc + c, (r-1) * nc + c);
            }
            if (r + 1 < nr && grid[r+1][c] == '1') {
              uf.union(r * nc + c, (r+1) * nc + c);
            }
            if (c - 1 >= 0 && grid[r][c-1] == '1') {
              uf.union(r * nc + c, r * nc + c - 1);
            }
            if (c + 1 < nc && grid[r][c+1] == '1') {
              uf.union(r * nc + c, r * nc + c + 1);
            }
          }
        }
      }
  
      return uf.getCount();
    }
  }
  

// @lc code=end

