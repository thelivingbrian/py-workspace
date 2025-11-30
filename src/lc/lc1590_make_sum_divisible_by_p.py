# Leetcode 1590 - Make Sum Divisible by P
# https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Keep a map %p -> the highest index who sum so far is key % p
        # At each element check if p = sum%p id in map 
        # Track minimum distance 
        total = sum(nums)
        extra = total % p
        if extra == 0: return 0
        
        minimum_distance = len(nums)
        cumulative = 0
        lookup = {0: -1}
        # nums: [3,1,4,2]    
        # cum: [3,4,2,4]    
        for index, num in enumerate(nums):
            
            cumulative = (cumulative + num) % p
            remainder = (cumulative-extra) % p # This is a tricky line

            if (remainder) in lookup:
                minimum_distance = min(minimum_distance, index-lookup[remainder])
            lookup[cumulative] = index
        return minimum_distance if minimum_distance < len(nums) else -1