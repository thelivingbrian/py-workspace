# LeetCode 678. Valid Parenthesis String
# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for character in s:
            if character == "(":
                low += 1
                high += 1
            elif character == ")":
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1

            low = max(low, 0)
            if high < 0:
                return False

        return low == 0