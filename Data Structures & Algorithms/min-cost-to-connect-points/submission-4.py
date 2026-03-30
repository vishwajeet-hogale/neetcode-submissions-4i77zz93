import heapq
# import math

class Solution:
    def distance(self, p1: List[int], p2: List[int]) -> float:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        
        ad_list = defaultdict(list)

        for i, p in enumerate(points):
            for j, q in enumerate(points):
                if i != j:
                    dis = self.distance(p, q)
                    ad_list[i].append((dis, j))
                    # ad_list[j].append((dis, i))

        heap = [(0,0)]
        cost = 0
        vis = set()
        while heap:
            curr_cost, curr_point = heapq.heappop(heap)
            if curr_point in vis:
                continue
            cost += curr_cost
            vis.add(curr_point)

            for neigh_cost, neigh in ad_list[curr_point]:
                if neigh not in vis:
                    heapq.heappush(heap, (neigh_cost, neigh))
        return cost




