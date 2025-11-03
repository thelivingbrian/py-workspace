# Leetcode 7373. Find K Pairs with Smallest Sums

# Original solution
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for i, num in enumerate(nums1):
            heapq.heappush(heap, (num + nums2[0], i, 0))

        out = []
        while heap and len(out) < k:
            total, index1, index2 = heapq.heappop(heap)
            if index2 + 1 < len(nums2):
                heapq.heappush(heap, (nums1[index1]+nums2[index2+1], index1, index2+1))
            out.append([nums1[index1], nums2[index2]])
        return out
    
