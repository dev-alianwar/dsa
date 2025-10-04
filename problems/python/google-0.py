from typing import List
import heapq
# Google interview problem
# You are given a list of airline tickets where each ticket is a pair [from, to].
# All tickets form at least one valid travel itinerary.
# The itinerary must:
# 1. Start from "JFK".
# 2. Use all tickets exactly once.
# 3. Be the lexicographically smallest possible itinerary (when multiple exist).
#
# Return the final travel path as a list of airport codes.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport: str):
            while airport in graph and graph[airport]:
                next_stop = heapq.heappop(graph[airport])
                dfs(next_stop)
            route.append(airport)

        dfs("JFK")
        return route[::-1]


tickets = [
    ["MUC", "LHR"],
    ["JFK", "MUC"],
    ["SFO", "SJC"],
    ["LHR", "SFO"]
]

solution = Solution()
result = solution.findItinerary(tickets)
print(result)