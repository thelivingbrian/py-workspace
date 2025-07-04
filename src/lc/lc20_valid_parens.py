# LeetCode 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range (len(s)):
            if s[i] == "(":
                stack.append("(")
            elif s[i] == ")":
                if len(stack) == 0 or stack.pop() != "(": return False
            elif s[i] == "[":
                stack.append("[")
            elif s[i] == "]":
                if len(stack) == 0 or stack.pop() != "[": return False
            elif s[i] == "{":
                stack.append("{")
            elif s[i] == "}":
                if len(stack) == 0 or stack.pop() != "{": return False
            else: 
                return False
            
        return len(stack) == 0