# Leetcode 3186. Maximum Total Spell Damage
# https://leetcode.com/problems/maximum-total-spell-damage/

# Incorrect - too slow w/o pruning current in dfs, otherwise wrong
 class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        total_for_damage = {}
        for spell in power: 
            if spell in total_for_damage:
                total_for_damage[spell] += spell
            else:
                total_for_damage[spell] = spell 

        def dfs(rem: Dict[int, int]) -> int: 
            if not rem: 
                return 0
            else: 
                highest = 0
                for damage, total in list(rem.items()): 
                    minus_two = rem.pop(damage-2, -1)
                    minus_one = rem.pop(damage-1, -1)
                    current = rem.pop(damage) # Could have been removed perminently via iteration in a previous depth search 
                    plus_one = rem.pop(damage+1, -1)
                    plus_two = rem.pop(damage+2, -1)
                    continuation = dfs(rem)
                    highest = max(highest, continuation + total)
                    if minus_two > 0: rem[damage-2] = minus_two
                    if minus_one > 0: rem[damage-1] = minus_one
                    #if current: rem[damage] = current
                    if plus_one > 0: rem[damage+1] = plus_one
                    if plus_two > 0: rem[damage+2] = plus_two
                return highest
        
        return dfs(total_for_damage)                   
                    
                    
# Fixes above problems - TLE
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        total_for_damage = {}
        for spell in power: 
            if spell in total_for_damage:
                total_for_damage[spell] += spell
            else:
                total_for_damage[spell] = spell 

        def dfs(rem: Dict[int, int]) -> int: 
            if not rem: 
                return 0
            else: 
                highest = 0
                for damage, total in list(rem.items()): 
                    rem.pop(damage)
                    new_rem = dict(rem)
                    for d in (damage-2, damage-1, damage+1, damage+2):
                        new_rem.pop(d, None)
                    continuation = dfs(new_rem)
                    highest = max(highest, continuation + total)
                return highest
        
        return dfs(total_for_damage)

# See Also: 
    # https://leetcode.com/problems/house-robber/
    # https://leetcode.com/problems/delete-and-earn/

# Memoized with lru-cache but still TLE
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        total_for_damage = {}
        for spell in power: 
            if spell in total_for_damage:
                total_for_damage[spell] += spell
            else:
                total_for_damage[spell] = spell 

        # 1, 1, 1, 4, 4, 6, 10, 11, 12 
        @lru_cache(maxsize=0)
        def max_from_index(index: int) -> int:
            if index >= len(power): return 0 
            following_end = bisect.bisect_right(power, power[index]+2)
            following_end2 = bisect.bisect_right(power, power[index]+3)
            following_end3 = bisect.bisect_right(power, power[index]+4)
            
            maximum = total_for_damage[power[index]] + max_from_index(following_end)
            if total_for_damage.get(power[index]+1, -1) > 0: 
                choose_one = total_for_damage[power[index]+1] + max_from_index(following_end2)
                maximum = max(maximum, choose_one)
            if total_for_damage.get(power[index]+2, -1) > 0: 
                choose_two = total_for_damage[power[index]+2] + max_from_index(following_end3)
                maximum = max(maximum, choose_two)
            return maximum 

        return max_from_index(0)

# DP solution - Accepted 
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counted = Counter(power)
        sorted_unique = sorted(counted)
        totals = [ val * counted[val] for val in sorted_unique]

        next_index = [0] * len(sorted_unique)
        for index, val in enumerate(sorted_unique):
            next_index[index] = bisect.bisect_right(sorted_unique, val+2)  

        # 30,  30,  20,  20,  18,  0
        dp = [0] * (len(sorted_unique) + 1)
        # 1,  3,  4,  5,  6
        # 4, 12, 16, 20, 18
        for i in range(len(sorted_unique)-1, -1, -1):
            keep = totals[i] + dp[next_index[i]] # 30
            skip = dp[i+1]                       # 20
            dp[i] = max(keep, skip)

        return dp[0]