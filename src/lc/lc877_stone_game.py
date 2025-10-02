# LeetCode 877. Stone Game
# https://leetcode.com/problems/stone-game/

# Magic solution 
#    Alice can compute the sum of the piles at even indices and the sum of the piles at odd indices up front.
#      because there are an odd number of stones there can never be a tie
#      Alice can always choose to take all even or odd parity indices, whichever is larger
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True