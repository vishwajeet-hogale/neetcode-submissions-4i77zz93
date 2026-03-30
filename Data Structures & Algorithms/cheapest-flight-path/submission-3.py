from collections import deque, defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        points_dis_map = [float('inf')]*n
        points_dis_map[src] = 0
        ad_list = defaultdict(list)
        for i,j, val in flights:
            ad_list[i].append([j,val])
        k += 1
        queue = deque()
        queue.append((src, 0))
        while queue and k:
            size = len(queue)
            for _ in range(size):
                node, cost = queue.popleft()

                for neigh, neigh_cost in ad_list[node]:
                    if neigh_cost + cost < points_dis_map[neigh]:
                        points_dis_map[neigh] = neigh_cost + cost
                        queue.append((neigh, neigh_cost + cost))
            k -= 1

        return -1 if points_dis_map[dst] == float('inf') else points_dis_map[dst]

