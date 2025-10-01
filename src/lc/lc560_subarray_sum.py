# LeetCode 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

# Original solution - based on map solution to g4g subarray sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulativeSums = defaultdict(list)
        cum_sum = 0
        total = 0
        for i, num in enumerate(nums):
            cum_sum += num 
            if cum_sum == k:
                total += 1
            if cum_sum - k in cumulativeSums:
                total += len(cumulativeSums[cum_sum - k])
            
            cumulativeSums[cum_sum].append(i)

        return total
    
# Cleaner code via chatgpt
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_qty = {0: 1} # in case first element matches
        total, count = 0, 0
        for num in nums:
            total += num
            count += sum_qty.get(total-k, 0)
            sum_qty[total] = sum_qty.get(total, 0) + 1
        return count