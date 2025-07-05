# LeetCode 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/

############
# Original solution (quadric, accepted but barely)

class Solution:
    def jump(self, nums: List[int]) -> int:
        index = 0
        minimum_list = [999999 for dest in nums]
        minimum_list[0] = 0
        while index < len(nums):
            minimum_to_arrive = minimum_list[index]
            for i in range (1, nums[index]+1):
                if index + i >= len(minimum_list): break
                minimum_list[index+i] = min(minimum_list[index+i], minimum_to_arrive+1)
            index += 1
        return minimum_list[-1]

#############
# Linear solution

class Solution1:
    def jump(self, nums: List[int]) -> int:
        index = 0
        jumps = 0 
        max_so_far = 1
        max_next_jump = 1
        while index < len(nums)-1: # skipping last index avoids need for early return
            max_next_jump = max(max_next_jump, index+nums[index]+1)
            if index == max_so_far -1:
                jumps, max_so_far = jumps+1, max_next_jump
            index +=1
        return jumps