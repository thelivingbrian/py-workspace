# LeetCode 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

############
#  Original solution

from typing import List

class Solution:
    cache = {}
    
    def generateParenthesis(self, n: int) -> List[str]:
        return self.combine(n, 0)

    def combine(self, rem: int, stack: int) -> List[str]:
        memo = self.cache.get((rem,stack))
        if memo != None:
            return memo
        elif rem == 0: 
            out = [ ")" * stack ]
            self.cache[(rem, stack)] = out
            return out
        else:
            out  = []
            out.extend( ["(" + item for item in self.combine(rem-1, stack+1)])
            if stack > 0:
                out.extend( [")" + item for item in self.combine(rem, stack-1)])
            self.cache[(rem, stack)] = out
            return out

############
#  Recursive solution with memoization - chatGPT

from functools import lru_cache

class Solution2:
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return [""]              # only the empty string
        out = []
        for i in range(n):
            # all ways to put i pairs inside the first ()…
            for left in self.generateParenthesis(i):
                # …and all ways to put the remaining (n−1−i) pairs after it
                for right in self.generateParenthesis(n-1-i):
                    out.append(f"({left}){right}")
        return out

#############

import sys

def run(n=3):
    sol = Solution()
    results = sol.generateParenthesis(n)
    print(f"Generated {len(results)} combinations of parentheses for n={n}:")
    for p in results:
        print(p)

if __name__ == "__main__":
    run()
