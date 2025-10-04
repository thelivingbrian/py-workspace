# Leetcode 11 - Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, highest = 0, len(height)-1, 0     # Do not need to track max index
        while l < r:
            box = min(height[l], height[r]) * (r - l)
            if box >= highest: 
                highest = box
            
            if height[l] < height[r]:           # Compare on current heights
                l+=1
            elif height[l] > height[r]:
                r-=1
            else:                               # Break ties (no recursion needed)
                l += 1
                r -= 1
        
        return highest