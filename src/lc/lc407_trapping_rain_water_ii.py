# LeetCode 407. Trapping Rain Water II
# https://leetcode.com/problems/trapping-rain-water-ii/

# "First" solution
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        W, L = len(heightMap[0]), len(heightMap)
        if W < 3 or L < 3: return 0
        
        seen = [[False for _ in range(W)] for _ in range(L)]
        boundary = []

        for y in range(L):
            seen[y][0] = True
            heapq.heappush(
                boundary,
                (heightMap[y][0], y, 0)
            )
            seen[y][-1] = True
            heapq.heappush(
                boundary,
                (heightMap[y][-1], y, W-1) # x spans from 0 to W-1
            )
            
        for x in range(W):
            seen[0][x] = True
            heapq.heappush(
                boundary,
                (heightMap[0][x], 0, x)
            )
            seen[-1][x] = True
            heapq.heappush(
                boundary,
                (heightMap[-1][x], L-1, x) # y spans from 0 to L-1
            )

        total_water = 0
        while boundary: 
            lowest_wall = heapq.heappop(boundary)
            h, y, x = lowest_wall[0], lowest_wall[1], lowest_wall[2]
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if y+dy < 0 or y+dy >= L or x+dx < 0 or x+dx >= W: continue
                if seen[y+dy][x+dx]: continue
                seen[y+dy][x+dx] = True
                if heightMap[y+dy][x+dx] < h:
                    total_water += h - heightMap[y+dy][x+dx]
                    heightMap[y+dy][x+dx] = h # This is the value that will get pushed
                heapq.heappush(
                        boundary, 
                        (heightMap[y+dy][x+dx], y+dy, x+dx)
                    )
        
        return total_water
    
# redo
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        L, W = len(heightMap), len(heightMap[0])
        if L<=2 or W <= 2: 
            return 0
        seen = [[False for _ in row] for row in heightMap]
        heap = []
        heapq.heapify(heap)

        for i in range(L):
            seen[i][0] = True
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            seen[i][-1] = True
            heapq.heappush(heap, (heightMap[i][-1], i, W-1))

        for i in range(1, W-1):
            seen[0][i] = True
            heapq.heappush(heap, (heightMap[0][i], 0, i))
            seen[-1][i] = True
            heapq.heappush(heap, (heightMap[-1][i], L-1, i))

        total = 0
        while heap:
            height, y, x = heapq.heappop(heap)
            for y2, x2 in [(y+1,x), (y-1, x),(y, x+1), (y, x-1)]:
                if y2 < 0 or y2 >= L or x2 < 0 or x2 >= W:
                    continue
                if seen[y2][x2]:
                    continue
                seen[y2][x2] = True
                current = heightMap[y2][x2]
                if current < height:
                    total += height - current
                    heapq.heappush(heap, (height, y2, x2))  # height is water level
                else:
                    heapq.heappush(heap, (current, y2, x2)) # current >= height

        return total