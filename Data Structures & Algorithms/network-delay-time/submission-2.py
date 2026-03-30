from collections import defaultdict, deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        ad_list = defaultdict(list)
        for i, j, cost in times:
            ad_list[i].append((j, cost))

        heap = [(0, k)]
        vis = set()
        cost = 0
        while heap:
            curr_cost, node = heapq.heappop(heap)
            if node in vis:
                continue
            cost = curr_cost

            vis.add(node)
            for neigh, cst in ad_list[node]:
                if neigh not in vis:
                    heapq.heappush(heap, (curr_cost + cst, neigh))

        return cost if len(vis) == n else -1
