# Leetcode 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

# original solution - TLE
class MedianFinder:
    def __init__(self):
        self.h = []
        heapq.heapify(self.h)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h, num)

    def findMedian(self) -> float:
        length = len(self.h)
        if length == 0: return 0.0   
        prev = result = self.h[0]
        store = []
        for i in range((length//2)+1):
            prev = result
            result = heapq.heappop(self.h)
            store.append(result)
        for item in store:
            heapq.heappush(self.h, item)
        isOdd = length % 2 == 1
        if isOdd:
            return float(result)
        else:
            return ( float(result) + float(prev) )/ 2 