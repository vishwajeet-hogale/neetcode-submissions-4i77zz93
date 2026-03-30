import heapq
# import math

class Solution:
    def distance(self, p1: List[int], p2: List[int]) -> float:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        ad_list = {i : [] for i in range(N)}

        for i in range(N):
            for j in range(i + 1, N):
                ad_list[i].append((self.distance(points[i], points[j]), j))
                ad_list[j].append((self.distance(points[i], points[j]), i))

        vis = set()
        cost = 0

        heap = [(0,0)]

        while len(vis) != N:
            curr_cost, curr_point = heapq.heappop(heap)
            if curr_point in vis:
                continue

            cost += curr_cost
            vis.add(curr_point)

            for neighCost, neigh in ad_list[curr_point]:
                if neigh not in vis:
                    heapq.heappush(heap, [neighCost, neigh])

        return cost
