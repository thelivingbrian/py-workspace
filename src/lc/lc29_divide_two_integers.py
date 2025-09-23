# Leetcode 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/

# Orignal solution (after initially getting TLE then bounds check issue)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        remainder = abs(dividend)
        div = abs(divisor)
        result = 0 
        i = 31 # Going to 32 uneeded 
        while i >= 0:
            if ( div << i ) <= remainder:
                remainder -= div << i
                result += ( 1 << i )
            i -= 1

        return max(-(1<<31), min((1<<31)-1, sign * result)) # Note 1 << 31
