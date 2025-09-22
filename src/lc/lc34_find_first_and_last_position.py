# LeetCode 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Original solution (no bisect, o(n) worst case)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l, r = 0, len(nums)-1
        index = -1
        while l <= r: 
            mid = (l + r) // 2
            if nums[mid] == target:
                index = l = r = mid
                break
            elif nums[mid] < target: 
                l = mid + 1 
            else: 
                r = mid - 1

        if index == -1: return [-1, -1]
        
        while l - 1 >= 0: # Must check bounds here 
            if nums[l-1] != target: break
            l -= 1
        while r + 1 < len(nums):
            if nums[r+1] != target: break 
            r += 1 

        return [l, r]

# With bisect (o(log n))
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = bisect.bisect_left(nums, target)
        if index >= len(nums) or nums[index] != target: return [-1, -1]
        return [index, bisect.bisect_right(nums, target)-1]

# ChatGpt
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft() -> int:
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    if nums[mid] == target:
                        ans = mid
                    r = mid - 1
            return ans

        def findRight() -> int:
            l, r = 0, len(nums) - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    if nums[mid] == target:
                        ans = mid
                    l = mid + 1
            return ans

        left, right = findLeft(), findRight()
        return [left, right]
