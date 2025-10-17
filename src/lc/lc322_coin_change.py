# Leetcode 322. Coin Change
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        @lru_cache(maxsize=None)
        def dfs(index: int, amount: int) -> int:
            if amount == 0:
                return 0
            if index >= len(coins) or amount < 0:
                return math.inf
            take = 1 + dfs(index, amount-coins[index])
            skip = dfs(index+1, amount)
            return min(take, skip)

        check = dfs(0, amount)
        return -1 if check == math.inf else check

# TLE class Solution:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 22 | 26 | 36 -> [10, 7, 4]
        coins.sort(reverse=True)
        
        @lru_cache(maxsize=None)
        def dfs(coins: Tuple[int], amount: int):
            minimum = math.inf
            for index, coin in enumerate(coins):
                maximum = amount // coin
                if amount % coin == 0: 
                    minimum = min(minimum, maximum)
                while maximum >= 0:
                    if maximum < minimum:
                        check = dfs(coins[index+1:], amount - (maximum*coin))
                        if check > 0:
                            minimum = min(minimum, maximum + check)
                    maximum -= 1
            if minimum == math.inf: return -1
            else: return minimum 

        coin_tuple = tuple(coins)
        return dfs(coin_tuple, amount)
                
# Also TLE
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 22 | 26 | 36 -> [10, 7, 4]
        coins.sort(reverse=True)
        
        @lru_cache(maxsize=None)
        def dfs(index: int, amount: int):
            minimum = math.inf
            if amount == 0: return 0
            if amount < 0 or index >= len(coins): return minimum
            maximum = amount // coins[index]
            while maximum >= 0:
                if maximum < minimum:
                    check = dfs(index+1, amount - (maximum*coins[index]))
                    minimum = min(minimum, maximum + check)
                maximum -= 1
            return minimum 

        result = dfs(0, amount)
        if result == math.inf: return -1
        else: return result

            