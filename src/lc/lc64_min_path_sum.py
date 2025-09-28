# LeetCode 64 - Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

# DP solution
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]

        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]
            
# First solution (slow)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        best_so_far = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(y, x, current):
            if best_so_far[y][x] == 0 or best_so_far[y][x] > current:
                best_so_far[y][x] = current 
                if y + 1 < len(grid):
                    dfs(y+1, x, current + grid[y+1][x])
                if x + 1 < len(grid[0]):
                    dfs(y, x+1, current + grid[y][x+1])
        
        dfs(0, 0, grid[0][0])
        return best_so_far[-1][-1]