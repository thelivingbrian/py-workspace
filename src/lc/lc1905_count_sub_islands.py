# LeetCode 1905 - Count Sub Islands
# https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        seen = [ [False for _ in range(len(grid1[i]))] for i in range(len(grid1))]

        def fill(y: int, x: int) -> bool:
            if y < 0 or y >= len(grid2) or x < 0 or x >= len(grid2[y]) or seen[y][x]: return True
            seen[y][x] = True   
            if grid2[y][x] != 1:
                return True
            else:
                ok = grid1[y][x] == 1 # See definition of sub-island - Do not early return False here
                return ok & fill(y+1, x) & fill(y-1, x) & fill(y, x+1) & fill(y, x-1)   # '&' because 'and' will short-circuit
                    
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                if seen[i][j] or grid2[i][j] == 0: 
                    continue
                else: 
                    if fill(i, j): count += 1
                    
        return count