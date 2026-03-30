from collections import deque, defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ad_list = defaultdict(list)
        for i,j, flight_cost in flights:
            ad_list[i].append([j, flight_cost])

        cost_map = [float('inf') for _ in range(n)]

        cost_map[src] = 0
        k += 1
        queue = deque([(src, 0)])
        while k and queue:
            size = len(queue)
            for _ in range(size):
                node, cost = queue.popleft()

                for adj_node, adj_cost in ad_list[node]:
                    if cost + adj_cost < cost_map[adj_node]:
                        cost_map[adj_node] = cost + adj_cost
                        queue.append((adj_node, cost + adj_cost))
            k -= 1
        return -1 if cost_map[dst] == float('inf') else cost_map[dst]