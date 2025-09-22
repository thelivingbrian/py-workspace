# LeetCode 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# First solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = len(nums)
        if nums[0] > nums[len(nums)-1]: # [4,5,6,7,0,1,2]
            l, r = 1, len(nums)-1
            while l < r:
                mid = (l + r) // 2
                if nums[mid-1] > nums[mid]:
                    l = r = mid
                elif nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            pivot = l 
        
        def binarySearch(lst: List[int], target: int) -> int:
            l, r = 0, len(lst)-1
            while l <= r: 
                mid = (l + r) // 2
                if lst[mid] == target: 
                    return mid
                elif lst[mid] < target: 
                    l = mid + 1
                else: 
                    r = mid - 1
            return -1
        
        if target < nums[0]:
            result = binarySearch(nums[pivot:], target)
            if result < 0: 
                return result
            else:
                return pivot + result 
        else:
            return binarySearch(nums[:pivot], target)


        