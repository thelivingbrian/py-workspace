# Leetcode 3397. Maximum Number of Distinct Elements after operations
# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

# Best version
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        maximum = -math.inf
        for num in nums: 
            difference = maximum - num 
            inc = max(0, difference+1)
            if inc <= 2*k:
                total += 1
                maximum = max(maximum, num + inc)
        return total

# Cleaner version
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        total, inc = 0, 0
        prev, maximum = -1, -1
        for num in nums: 
            if num != prev: # Prev is not being set so this is always true
                difference = maximum - num 
                inc = max(0, difference+1)
            if inc <= 2*k:
                total += 1
                maximum = max(maximum, num + inc)
            inc += 1
        return total

# "Cleaner" version - feels fragile
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prev = maximum = nums[0]
        unique = set([prev])
        inc = min(k, 1)  # index 1 may match index 0, but also k might be 0
        for num in nums[1:]: 
            if num != prev:
                prev = num
                difference = maximum-num
                inc = max( 0, min(difference+1, 2*k))  # is in [0, 2k] and [0, difference] used                
            value = num + inc
            maximum = max(maximum, value)
            unique.add(value)
            if inc < 2 * k: 
                inc += 1
        return len(unique)

# Original solution
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # Sort numbers to group duplicates
        nums.sort()
        # [ 1, 1, 1, 4, 4, 4, 6, 6 ]
        # - k = 1       # Can skip this step without loss of generality
        # [0, 0, 0, 3, 3, 3, 5, 5 ] 
        # add up to 2k for each dupe
        # [0, 1, 2, 3, 4, 5, 5, 6]
        # make sure to start from max seen so far
        prev = -1
        maximum = -1
        inc = 0 
        unique = set()
        for num in nums: 
            if num != prev:
                prev = num
                if maximum >= num: # [1,2,2,3,3,4]
                    inc = min((maximum-num)+1, 2*k)
                else:
                    maximum = num
                    inc = 0         
            value = num + inc
            maximum = max(maximum, value)
            unique.add(value)
            if inc < 2*k:
                inc += 1
        return len(unique)