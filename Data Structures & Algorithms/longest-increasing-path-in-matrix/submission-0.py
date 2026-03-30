from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        def bfs(i,j):
            local_max = 1
            queue = deque([(i,j, 1)])
            vis = set()
            directions = [
                (1,0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]
            while queue:
                size = len(queue)
                # print("Inside")
                # print(queue)
                for _ in range(size):
                    x, y, path_len = queue.popleft()
                    # vis.add((x,y))
                    
                    for ix, iy in directions:
                        r, c = x + ix, y + iy
                        if 0 <= r < n and 0 <= c < m :
                            if matrix[r][c] > matrix[x][y]:
                                queue.append((r, c, path_len + 1))
                                local_max = max(local_max, path_len + 1)
                                

            return local_max

        mlen = 1
        # print(bfs(0,0))
        for i in range(n):
            for j in range(m):
                mlen = max(mlen, bfs(i,j)) 

        return mlen

            


        