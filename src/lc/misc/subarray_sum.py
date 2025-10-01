# https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1

# See also: Leetcode 560 - Subarray Sum Equals K

# original solution
class Solution:
    def subarraySum(self, arr, target):
        i, j = 0, 1
        total = arr[0]
        while i < len(arr):
            if total == target: 
                return [i+1,j]
            if total < target and j < len(arr): 
                total += arr[j]
                j = j+1
            else: 
                total -= arr[i]
                i += 1
        return [-1]
    
# handles 0 cases that g4g does not include test cases for:
class Solution:
    def subarraySum(self, arr, target):
        if target <= 0: 
            for n in range(len(arr)): 
                if arr[n] == target: return [n+1,n+1]
            return [-1]
        
        i, j, total = 0, 0, 0
        while i < len(arr):
            if total == target: 
                return [i+1,j]
            if total < target and j < len(arr): 
                total += arr[j]
                j = j+1
            else: 
                total -= arr[i]
                i += 1
        return [-1]
    
# Devin - Dictionary solution (see also: Lc560)
    def _subarrySum_hashingAndPrefixSum(self, arr, target):
        sum_map = {}
        cumulative_sum = 0

        for i, num in enumerate(arr):
            cumulative_sum += num
            
            if cumulative_sum == target:
                return [
                    1, 
                    (i+1)
                ]
            if (cumulative_sum - target) in sum_map:
                start = sum_map[cumulative_sum - target] + 1
                return [
                    (start+1), 
                    (i+1)
                ]
            if cumulative_sum not in sum_map:
                sum_map[cumulative_sum] = i
                
        return [-1]