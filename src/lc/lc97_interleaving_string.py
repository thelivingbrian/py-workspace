#LeetCode 97. Interleaving String
#https://leetcode.com/problems/interleaving-string/

class Solution:
    @lru_cache(maxsize=None)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s3 == "": 
            return s1 == "" and s2 == ""
        if s2 != "" and s3[0] == s2[0]:
            if self.isInterleave(s1, s2[1:], s3[1:]): return True
        if s1 != "" and s3[0] == s1[0]:
            if self.isInterleave(s1[1:], s2, s3[1:]): return True
        return False


# Manual memoization (Un-memoized version will get TLE)
class Solution:
    def __init__(self):
        self.memo = {} # Must use instance variable, not class variable

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "": return s2 == s3
        if s2 == "": return s1 == s3
        if s3 == "": return False
        if (s1, s2) in self.memo: return self.memo[(s1,s2)]
        
        result = False
        if s1[0] == s3[0]:
            result = self.isInterleave(s1[1:], s2, s3[1:])  # Don't early return
        if s2[0] == s3[0] and not result:                   # Don't overwrite if already True
            result = self.isInterleave(s1, s2[1:], s3[1:])
        
        self.memo[(s1,s2)] = result
        return result