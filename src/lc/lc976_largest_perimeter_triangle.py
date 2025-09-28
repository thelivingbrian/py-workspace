# 976. Largest Perimeter Triangle
# https://leetcode.com/problems/largest-perimeter-triangle/

# O(n Logn) solution - brute force will TLE 
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        side_lengths = sorted(nums, reverse=True)

        maximum = 0
        for i in range(len(side_lengths)-2):
            # Largest permimeter triangle will have consecutive sides
            #   because if [i+1] + [i+2] < [i] then subsequent indexes will be even smaller 
            if side_lengths[i] < side_lengths[i+1] + side_lengths[i+2]:
                maximum = max(maximum, side_lengths[i] + side_lengths[i+1] + side_lengths[i+2])
        
        return maximum