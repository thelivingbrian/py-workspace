# Leetcode 3186. Maximum Total Spell Damage
# https://leetcode.com/problems/maximum-total-spell-damage/

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

# See Also: 
    # https://leetcode.com/problems/house-robber/
        # Backward
        class Solution:
            def rob(self, nums: List[int]) -> int:
                dp = [0] * (len(nums)+2)
                
                # 12, 10, 10, 3, 1, 0, 0
                # 2, 7, 9, 3, 1
                for i in range(len(nums)-1, -1, -1):
                    skip = dp[i+1]
                    keep = nums[i] + dp[i+2]
                    dp[i] = max(skip, keep)

                return dp[0]
        # Forward
        class Solution:
            def rob(self, nums: List[int]) -> int:
                size = len(nums)
                if size <= 2: return max(nums)

                dp = [0] * size
                dp[0], dp[1] = nums[0], max([nums[1], nums[0]])
                
                # 2, 2, 3, 4
                # 2, 1, 1, 2
                for i in range(2, size):
                    skip = dp[i-1]
                    keep = nums[i] + dp[i-2]
                    dp[i] = max(skip, keep)

                return dp[-1]
        # O(1) space
        class Solution:
            def rob(self, nums: List[int]) -> int:
                prev2 = prev1 = 0
                for num in nums:
                    prev2, prev1 = prev1, max(prev1, num + prev2)
                return prev1
    # https://leetcode.com/problems/delete-and-earn/


# Invalid TLE solutions:                   
                    
# TLE w/ Dictionary DFS
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
                    new_rem = dict(rem) # Must create copy since iteration is removing elements
                    for d in (damage-2, damage-1, damage+1, damage+2):
                        new_rem.pop(d, None)
                    continuation = dfs(new_rem)
                    highest = max(highest, continuation + total)
                return highest
        
        return dfs(total_for_damage)


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


# ChatGPT Solutions (accepted)
class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        # 1) compress
        cnt = Counter(power)
        sum_at = {d: d * c for d, c in cnt.items()}

        # 2) sort unique damages
        keys = sorted(sum_at.keys())
        m = len(keys)
        if m == 0:
            return 0

        # 3) precompute prev index for each i using binary search
        prev = []
        for i, d in enumerate(keys):
            j = bisect.bisect_right(keys, d - 3) - 1  # last index <= d-3
            prev.append(j)

        # 4) DP
        dp = [0] * m
        for i in range(m):
            take = sum_at[keys[i]] + (dp[prev[i]] if prev[i] >= 0 else 0)
            skip = dp[i - 1] if i > 0 else 0
            dp[i] = max(skip, take)

        return dp[-1]

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0

        # 1) Combine duplicates: total contribution if we choose damage d is d * count(d)
        count_by_damage = Counter(power)
        damage_values = sorted(count_by_damage.keys())
        total_at_damage = [d * count_by_damage[d] for d in damage_values]

        # 2) For each position i, find the last index j with damage_values[j] <= damage_values[i] - 3
        prev_compatible_index: List[int] = []
        for i, d in enumerate(damage_values):
            j = bisect.bisect_right(damage_values, d - 3) - 1
            prev_compatible_index.append(j)

        # 3) Memoized recursion over index in damage_values
        @lru_cache(maxsize=None)
        def best_total_up_to(index: int) -> int:
            """
            Returns the maximum total damage considering damage_values[0..index].
            """
            if index < 0:
                return 0

            # Option A: skip current damage bucket
            skip_current = best_total_up_to(index - 1)

            # Option B: take current damage bucket and jump to its last compatible predecessor
            take_current = total_at_damage[index] + best_total_up_to(prev_compatible_index[index])

            return max(skip_current, take_current)

        return best_total_up_to(len(damage_values) - 1)

