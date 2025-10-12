# Leetcode 139. Word Break
# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(maxsize=None)
        def is_valid(part:str) -> bool:
            if len(part) == 0: return True
            for index in range(len(part)):
                if part[:index+1] in wordDict:
                    if is_valid(part[index+1:]): # Do not early return
                        return True
            return False
        return is_valid(s)