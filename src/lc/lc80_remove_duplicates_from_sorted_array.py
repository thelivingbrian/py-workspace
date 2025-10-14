# Leetcode 80. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Simplified solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        write = 2
        # 1, 1, 4, 4, 4, 5, 7
        for index in range(2, len(nums)):
            if nums[index] != nums[write-2]:
                nums[write] = nums[index]
                write += 1
        
        return write 
    
#Original solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return 2
        # 1, 1, 1, 2, 2, 3
        write = 2
        have_placeholder = False
        placeholder = nums[1] # handles case where no placeholder is set
        for index in range(2, len(nums)):
            if nums[index] == nums[index-1] and nums[index-1] == nums[index-2]:
                continue     
            if index > write:
                if have_placeholder: nums[write-1] = placeholder
            placeholder = nums[index]
            have_placeholder = True
            write += 1
        
        if write != len(nums): # Could be a long string at beginning where no placeholder was set
            nums[write-1] = placeholder
        return write
    
# Different flag logic 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return 2
        # 1, 1, 1, 2, 2, 3
        write = 2
        placeholder = 0
        for index in range(2, len(nums)):
            if nums[index] == nums[index-1] and nums[index-1] == nums[index-2]:
                continue     
            if index > write:
                if write > 2: nums[write-1] = placeholder
            placeholder = nums[index]
            write += 1
        
        if write > 2:
            nums[write-1] = placeholder
        return write
    
# See Also: LC82

