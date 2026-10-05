# LeetCode 856. Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for character in s:
            if character == "(":
                stack.append(0)
            else:
                top = stack.pop()
                parent = stack.pop()
                stack.append(parent + max(2 * top, 1))

        return stack.pop()