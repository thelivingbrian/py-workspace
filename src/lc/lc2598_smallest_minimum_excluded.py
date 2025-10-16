# Leetcode 2598. Smallest Missing Non-negative Integer After Operations
# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counts = Counter(num%value for num in nums) # Duplicates can push MEX higher than value 
        minimum = min(counts.get(i,0) for i in range(value))
        for guess in range(value):
            count = counts.get(guess, 0)
            if count == minimum:
                return guess + count * value
        return -1