# Leetcode 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

# Unsolved - chatgpt suggestion 
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3: 
            return 0

        l, r = 0, n - 1
        left_max, right_max = 0, 0
        water = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1
        return water

# original solution
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height)-1
        left_wall, right_wall = l, r
        while l <= r:
            if height[left_wall] < height[right_wall]:
                if height[l] >= height[left_wall]:
                    left_wall = l
                else:
                    water += height[left_wall] - height[l]
                l += 1
            else: 
                if height[r] >= height[right_wall]:
                    right_wall = r
                else:
                    water += height[right_wall] - height[r]
                r -= 1
        return water 

# Weird edge case tolerance 
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height)-1
        left_wall, right_wall = 0, 0
        while l <= r:
            if left_wall < right_wall:      # requires while l <= r or misses middle element
            # if height[l] < height[r]:     # while l < or <= r works here (why? b.c. last cell cannot trap water)
                if height[l] >= left_wall:
                    left_wall = height[l]
                else:
                    water += left_wall - height[l]
                l += 1
            else: 
                if height[r] >= right_wall:
                    right_wall = height[r]
                else:
                    water += right_wall - height[r]
                r -= 1
        return water 

# chatGPT Monotonic Stack solution - very confusing at first 
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # indices, heights increasing
        water = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h: # Keep popping until h is left wall
                bottom = stack.pop()
                if not stack: 
                    break
                left = stack[-1]
                width = i - left - 1
                bounded_height = min(height[left], h) - height[bottom] # Everything below the height of the bottom is already filled with water
                water += width * bounded_height
            stack.append(i)
        return water

# follow up
# Suppose a '0' in the input means that there is a leak at that position 
# and the water can leak out. After the adjustment, that is, after the 
# water levels have stabilized due to leaking, what is the answer?

# How do we change our approach/what would be out ideal answer 
# for this scenario?

# A: Split the array into subarrays at the 0s and sum the results of each subarray
