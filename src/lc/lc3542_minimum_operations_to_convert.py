# Leetcode 3542. Minimum Operations to Convert all Elements to 0
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

# Stack solution
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        total = 0
        for num in nums: 
            while stack and stack[-1] > num:
                stack.pop()
            if num == 0:
                continue
            elif stack and stack[-1] == num:
                continue
            else:
                total += 1
                stack.append(num)
        return total

# Original attempt - TLE
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = sorted(list(set(nums)))
        total = 0
        for number in s:
            if number == 0: continue   
            for index in range(len(nums)):                    
                if nums[index] == number:
                    total += 1
                    while index < len(nums) and nums[index] >= number:
                        if nums[index] == number:
                            nums[index] = 0
                        index += 1
        return total 