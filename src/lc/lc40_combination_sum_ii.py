# Leetcode 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

# Original solution 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort / add tuples to set 
        sorted_lst = sorted(candidates)
        combinations = self.combinationSumSorted(sorted_lst, target)
        return [ list(combo) for combo in combinations ]  

    def combinationSumSorted(self, candidates: List[int], target: int) -> Set[Tuple[int]]:
        out = set()
        for index in range(len(candidates)): 
            if index > 0 and candidates[index] == candidates[index-1]: continue # Without this line TLE
            if candidates[index] == target:
                out.add((candidates[index],))
            elif candidates[index] < target:
                new_target = target - candidates[index]
                rest = self.combinationSumSorted(candidates[index+1:], new_target)
                for combo in rest:
                    entry = (candidates[index],)
                    out.add(entry+combo)
            else: 
                break
        return out  

# With DFS
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        def dfs(start: int, target: List[int], path: List[int]):
            if target == 0: 
                out.append(path)
            
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index-1]: 
                    continue
                if candidates[start] > target: 
                    break
                else:
                    dfs(index+1, target-candidates[index], path + [candidates[index]])
        
        dfs(0, target, [])
        return out

# Mutate Path 
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        candidates.sort()

        path = []
        def dfs(start: int, target: List[int]):
            if target == 0: 
                out.append(path[:]) # copy
            
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index-1]: 
                    continue
                if candidates[start] > target: 
                    break
                else:
                    path.append(candidates[index])
                    dfs(index+1, target-candidates[index])
                    path.pop()
        
        dfs(0, target)
        return out

# Chatgpt
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res, path = [], []

        def dfs(start: int, remain: int) -> None:
            if remain == 0:
                res.append(path[:])     # copy once
                return
            # iterate next choices
            for i in range(start, len(candidates)):
                # skip duplicates at the *same depth*
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                val = candidates[i]
                if val > remain:
                    break                # further ones are larger (sorted)
                path.append(val)
                dfs(i + 1, remain - val) # each number can be used once
                path.pop()

        dfs(0, target)
        return res