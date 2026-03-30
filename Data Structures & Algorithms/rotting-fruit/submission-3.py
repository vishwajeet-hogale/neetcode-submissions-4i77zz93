from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        rotten_pos = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 2]
        fresh_cnt = sum(1 for i in range(n) for j in range(m) if grid[i][j] == 1)

        def bfs():
            queue = deque(rotten_pos)  
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            cnt = 0
            nonlocal fresh_cnt

            while queue and fresh_cnt > 0:
                size = len(queue)
                for _ in range(size):
                    curr_i, curr_j = queue.popleft()
                    for di, dj in directions:
                        new_i, new_j = curr_i + di, curr_j + dj
                        if 0 <= new_i < n and 0 <= new_j < m and grid[new_i][new_j] == 1:
                            grid[new_i][new_j] = 2
                            fresh_cnt -= 1
                            queue.append((new_i, new_j))
                cnt += 1

            return cnt

        res = bfs()
        return -1 if fresh_cnt else res