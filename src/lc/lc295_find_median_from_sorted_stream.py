# Leetcode 295. Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

# Two heap solution
class MedianFinder:
    def __init__(self):
        self.low = []  # 5, 4, 3, 2
        self.high = [] # 7, 8, 10 

    def addNum(self, num: int) -> None:
        if len(self.low) + len(self.high) == 0:
            heapq.heappush(self.low, -num)
        elif len(self.low) == len(self.high):
            if num <= -self.low[0]:
                heapq.heappush(self.low, -num)
            else:
                heapq.heappush(self.high, num)
        elif len(self.low) > len(self.high):
            if num <= -self.low[0]:
                heapq.heappush(self.low, -num)
                heapq.heappush(self.high, -heapq.heappop(self.low))
            else:
                heapq.heappush(self.high, num)
        else: # High has more elements
            if num <= -self.low[0]:
                heapq.heappush(self.low, -num)
            else:
                heapq.heappush(self.high, num)
                heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) + len(self.high) == 0:
            return 0
        elif len(self.low) == len(self.high):
            return float(-self.low[0]+self.high[0]) / 2
        elif len(self.low) > len(self.high):
            return float(-self.low[0])
        else: # High has more elements
            return float(self.high[0])

# original attempt - TLE
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