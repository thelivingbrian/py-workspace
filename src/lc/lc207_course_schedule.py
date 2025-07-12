# LeetCode 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

# Interesting and worth redoing - optimization is tricky / Or is it? Orig solution differs only in set reuse essentially 

# Original solution
class Solution:
    loop_free_cache = set({})
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.loop_free_cache = set({})
        g = defaultdict(list)
        for prereq in prerequisites: 
            g[prereq[0]].append(prereq[1])

        for i in range(numCourses): 
            if i in self.loop_free_cache: continue
            seen = set({i}) 
            if self.dfs(i, g, seen) == False: return False
        
        return True


    def dfs(self, current, graph, seen) -> bool: 
        for course in graph[current]: 
            if course in seen: return False
            if course in self.loop_free_cache: continue
            loop_free = self.dfs(course, graph, seen | {course})
            if not loop_free: return False
        self.loop_free_cache.add(current)
        return True

# Final solution - meh 
class Solution:
    visiting, visited = set(), set()
    graph = {}
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visiting, self.visited = set(), set()
        
        self.graph = defaultdict(list)
        for prereq in prerequisites: 
            self.graph[prereq[0]].append(prereq[1])

        for i in range(numCourses): 
            if not self.dfs(i): return False
        
        return True


    def dfs(self, current) -> bool: 
        if current in self.visiting: return False
        if current in self.visited: return True 
        
        self.visiting.add(current)
        for course in self.graph[current]: 
            loop_free = self.dfs(course)
            if not loop_free: return False
        self.visiting.remove(current)
        self.visited.add(current)
        return True

# Copilot solution - Much faster
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        if not prerequisites: return True
        dic = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            dic[course].append(prereq)

        visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for prereq in dic[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

# ChatGPT solution
from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build forward adjacency list
        graph = defaultdict(list)
        for dest, src in prerequisites:          # course A depends on B  ⇒  edge A → B
            graph[dest].append(src)

        WHITE, GRAY, BLACK = 0, 1, 2             # 0 = unseen, 1 = on call-stack, 2 = done
        color = [WHITE] * numCourses             # index = course id

        def dfs(v: int) -> bool:                 # True ⇒ no cycle beneath v
            if color[v] == GRAY:                 # back-edge → cycle
                return False
            if color[v] == BLACK:                # already proved safe
                return True

            color[v] = GRAY                      # mark “in progress”
            for nxt in graph[v]:
                if not dfs(nxt):
                    return False
            color[v] = BLACK                     # finished v’s sub-tree safely
            return True

        for course in range(numCourses):         # in case the graph isn’t fully connected
            if color[course] == WHITE and not dfs(course):
                return False
        return True
