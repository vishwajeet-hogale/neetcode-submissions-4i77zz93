from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        n, m = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(i, j):
            queue = deque([(i, j)])
            board[i][j] = 'T'  # mark as safe

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    r, c = x + dx, y + dy
                    if 0 <= r < n and 0 <= c < m and board[r][c] == 'O':
                        board[r][c] = 'T'
                        queue.append((r, c))

        # 1. Run BFS from boundary 'O's
        for i in range(n):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][m-1] == 'O':
                bfs(i, m-1)

        for j in range(m):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[n-1][j] == 'O':
                bfs(n-1, j)

        # 2. Flip remaining 'O' → 'X'
        # 3. Convert 'T' back → 'O'
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'