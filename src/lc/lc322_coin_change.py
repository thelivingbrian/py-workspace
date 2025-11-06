# Leetcode 322. Coin Change
# https://leetcode.com/problems/coin-change/

# DFS 
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

# BFS - Faster. More natural? Arguably best solution. 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Nodes are amounts, Edge weights are coins
        if amount == 0: return 0
        queue = deque([[0,0]])
        seen = set([0])
        while queue:
            total, coin_count = queue.popleft()
            for coin in coins:
                new_total = total + coin
                if new_total == amount:
                    return coin_count + 1 # First occurance must take fewest number of steps 
                elif new_total < amount and new_total not in seen:
                    seen.add(new_total)
                    queue.append([new_total, coin_count+1])
        return -1

# Bottom-up DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_array = [amount+1] * (amount + 1)
        dp_array[0] = 0 
        for i in range(1, amount+1):
            for coin in coins:
                if coin > i: 
                    continue
                dp_array[i] = min(dp_array[i], 1 + dp_array[i-coin])
        
        result = dp_array[-1]
        if result > amount:
            return -1
        return result

###
# Attempt reference -

# TLE
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

            