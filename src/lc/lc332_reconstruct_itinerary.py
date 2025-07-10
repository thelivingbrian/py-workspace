# LC332 Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/


# Accepted - Heirholzer's algorithm
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.sorted = False

class Edge: 
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {}
        sorted_tickets = sorted(tickets, reverse=True) 
        for ticket in sorted_tickets:
            node_from = dic.get(ticket[0])
            if node_from is None:
                node_from = Node(ticket[0])
                dic[ticket[0]] = node_from
            node_to = dic.get(ticket[1])
            if node_to is None:
                node_to = Node(ticket[1])
                dic[ticket[1]] = node_to
            edge = Edge(node_from, node_to)
            node_from.edges.append(edge)

        current = start = dic["JFK"]
        itinerary = []
        self.dfs(start, itinerary)
        return itinerary[::-1]

    def dfs(self, current_node, itinerary):
        while current_node.edges:
            self.dfs(current_node.edges.pop().to_node, itinerary)
        itinerary.append(current_node.name)

        
# Original solution - TLE 
class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.sorted = False

class Edge: 
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {}
        for ticket in tickets:
            node_from = dic.get(ticket[0])
            if node_from is None:
                node_from = Node(ticket[0])
                dic[ticket[0]] = node_from
            node_to = dic.get(ticket[1])
            if node_to is None:
                node_to = Node(ticket[1])
                dic[ticket[1]] = node_to
            edge = Edge(node_from, node_to)
            node_from.edges.append(edge)

        start = dic["JFK"]
        seen = set({})
        n = len(tickets)
        return self.serializePath(start, seen, 0, n)

    def serializePath(self, current_node, seen, depth, n) -> List[str]:
        if depth > n: return []
        if depth == n: return [current_node.name]
        if not current_node.sorted:
            current_node.edges.sort(key = lambda edge: edge.to_node.name)
            current_node.sorted = True
        for edge in current_node.edges:
            if edge in seen: continue
            seen.add(edge)
            resp = self.serializePath(edge.to_node, seen, depth+1, n)
            if len(resp) > 0:
                out = [current_node.name]
                out.extend(resp)
                return out
            seen.remove(edge)
        return []
