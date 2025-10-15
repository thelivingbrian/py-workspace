# Leetcode 3349. Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1: return True
        prev = nums[0]
        count = 1
        total = 0
        for num in nums[1:]:
            if num > prev:
                count += 1
                if count % k == 0:
                    total += 1
                if total == 2:
                    return True
            else:
                if count < k: total = 0 # Subarrays must be adjacent
                count = 1
            prev = num
        return False
    
# LC3350. Adjacent Increasing Subarrays Detection II
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

# First Solution
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        sequence_lengths = []
        streak = 1
        prev = nums[0]
        for num in nums[1:]:
            if num > prev:
                streak += 1
            else:
                sequence_lengths.append(streak)
                streak = 1
            prev = num
        sequence_lengths.append(streak)
        
        max_adjacent = sequence_lengths[0] // 2
        for i in range(1, len(sequence_lengths)):
            minimum = min(sequence_lengths[i], sequence_lengths[i-1])
            max_adjacent = max([max_adjacent, sequence_lengths[i]//2, minimum])
        
        return max_adjacent

# O(1) Space solution
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        out = 0
        streak = prev_streak = 1
        prev = nums[0]
        for num in nums[1:]:
            if num > prev:
                streak += 1
            else:
                out = max( out, streak//2, min(streak, prev_streak))
                prev_streak = streak
                streak = 1
            prev = num
        
        return max( out, streak//2, min(streak, prev_streak))

# Binary search solution (Why?) nlogn time, n space - confusing
class Solution:
    def check(self, v, k):
        for i in range(len(v) - k):
            # Check for a value in dp that is at least k, and the value k indices away is also at least k
            # e.g. k=3, arr = [1,2,3,1,2,3] -> dp = [1,2,3,1,2,3] => True: i[2] & i[2+k] >= k
            if v[i] >= k and v[i + k] >= k:
                return True
        return False

    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        if n == 2:
            return 1

        dp = [1] * n
        for i in range(1, n):
            # Maximum length of increasing subarray ending at index i
            if nums[i] <= nums[i - 1]:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + 1

        ans = 1
        low, high = 1, n // 2 # k must be at least 1, at most n//2

        # Binary search the range of valid k values
        while low <= high:
            mid = low + (high - low) // 2
            if self.check(dp, mid):
                ans = mid # Passes sliding window check, try for a larger k
                low = mid + 1
            else:
                high = mid - 1
        return ans