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