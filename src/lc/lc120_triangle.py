# Leetcode 120. Triangle
# https://leetcode.com/problems/triangle/

# Original solution 
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
#            2
#            3 4
#            6 5 7
#            4 1 8 3

#            2
#            5  6
#            11 10 13
#            15 11 18 16
        dp = [[100_000_000 for _ in row] for row in triangle] # Entries can be negative (but triangle is 200 rows high and entries < 10^5)
        dp[0] = triangle[0]
        for index, layer in enumerate(dp[:-1]):
            for n, entry in enumerate(layer):
                if dp[index+1][n] > entry + triangle[index+1][n]:
                    dp[index+1][n] = entry + triangle[index+1][n]
                if dp[index+1][n+1] > entry + triangle[index+1][n+1]:
                    dp[index+1][n+1] = entry + triangle[index+1][n+1]
        return min(dp[-1])