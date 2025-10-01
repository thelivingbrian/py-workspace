# https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1

# Original 
class Solution:
    def pushZerosToEnd(self, arr):
        read, write, trailing_zeros = 0, 0, 0
        while read < len(arr):
            if arr[read] != 0:
                if write != read: arr[write] = arr[read]
                read += 1
                write += 1
                continue
            else:
                trailing_zeros += 1
                read += 1
                
        for i in range(1, trailing_zeros+1):
            arr[-i] = 0

# same logic - no redundant variables 
class Solution:
    def pushZerosToEnd(self, arr):
        write = 0
        for read in range(len(arr)):
            if arr[read] != 0:
                if write != read: arr[write] = arr[read]
                write += 1
                continue
                
        for i in range(write, len(arr)):
            arr[i] = 0

# Is also leetcode 283 - Move Zeroes
# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read_pos, write_pos = 0, 0
        while read_pos < len(nums):
            if nums[read_pos] != 0:
                if read_pos != write_pos: 
                    nums[write_pos] = nums[read_pos]
                write_pos += 1
            read_pos += 1
        
        for i in range(write_pos, len(nums)):
            nums[i] = 0