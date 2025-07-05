# Leetcode 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

# This one is tricky - look up Kandane's algorithm for reference

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_streak = max_sub = nums[0]
        for num in nums[1:]:
            max_streak = max(num, max_streak+num)
            max_sub = max(max_sub, max_streak)
        return max_sub
