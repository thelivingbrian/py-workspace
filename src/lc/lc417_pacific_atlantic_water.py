# Leetcode 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 00 Pacific / Atlantic 
        seen = [[0 for _ in heights[0]] for _ in heights]
        
        def dfs(y: int, x: int, side: int): 
            if seen[y][x] & side: # This side's bit is already set - move on
                return
            seen[y][x] |= side    # Ocean has made it this far
            for dy, dx in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                if y+dy < 0 or x+dx < 0 or y+dy>=len(heights) or x+dx>=len(heights[y]):
                    continue
                if heights[y][x] <= heights[y+dy][x+dx]: 
                    dfs(y+dy, x+dx, side)
        
        # Flow upward from the oceans instead of downward from each cell 
        for i in range(len(heights)): 
            dfs(i, 0, 2)
            dfs(i, len(heights[0])-1, 1)

        for j in range(len(heights[0])): 
            dfs(0, j, 2)
            dfs(len(heights)-1, j, 1)    

        out = []
        for i in range(len(heights)): 
            for j in range(len(heights[0])): 
                if seen[i][j] == 3: out.append([i,j])  # Both bits are flipped (11 == 3)
        return out