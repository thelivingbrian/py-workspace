# LeetCode 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

# Linear Time (cool)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for num in s:
            if num - 1 not in s:          # only start at a run’s left edge
                di = 0 
                while num + di in s:
                    di += 1
                best = max(best, di)
        return best


#Original solution - O(n log n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0 
        # Not O(n) time because of sort 
        nums.sort()
        longest = 1
        current = 1 
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1: 
                current += 1
                longest = max(longest, current)
            elif nums[i+1] == nums[i]:
                continue
            else:
                current = 1 
        return longest

# Wonky - Time Complexity unclear, chatGPT says O(n^2) worst case 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0 
        dic = {}
        maximum = 1
        for num in nums:
            previous_sequence = dic.get(num-1)
            next_sequence = dic.get(num+1)
            if previous_sequence is None and next_sequence is None: 
                dic[num] = set([num])
            elif previous_sequence is not None and next_sequence is not None:
                new_set = previous_sequence | next_sequence | set({num})
                maximum = max(maximum, len(new_set))
                dic[num] = new_set
                i = num - 1
                while True:
                    check = dic.get(i)
                    if check is None: 
                        break 
                    dic[i] = new_set 
                    i -= 1
                j = num + 1
                while True:
                    check = dic.get(j)
                    if check is None: 
                        break 
                    dic[j] = new_set 
                    j += 1
            elif previous_sequence is not None:
                previous_sequence.add(num)
                maximum = max(maximum, len(previous_sequence))
                dic[num] = previous_sequence
            else: 
                next_sequence.add(num)
                maximum = max(maximum, len(next_sequence))
                dic[num] = next_sequence
        return maximum 
        