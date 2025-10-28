# LeetCode 55 Jump Game
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_allowed = 1
        index = 0
        while index < max_allowed and index < len(nums):
            max_allowed = max(max_allowed, index + nums[index] + 1) # Note: +1 
            index += 1
        return max_allowed >= len(nums)
    
# redo 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = 0
        for index, num in enumerate(nums):
            if index > maximum: return False
            maximum = max(maximum, index + num)
        return True