class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["." for _ in range(n)] for _ in range(n)]
        res = []
        def check_goal(grid):
            # Count number of 'Q' on the board
            q_count = sum(1 for i in range(n) for j in range(n) if grid[i][j] == "Q")
            return q_count == n

        def check(grid, i, j):
            # Check vertically (same column j)
            for r in range(n):
                if r != i and grid[r][j] == "Q":
                    return False

            # Check horizontally (same row i)
            for c in range(n):
                if c != j and grid[i][c] == "Q":
                    return False

            # Check diagonals
            for di, dj in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                curr_i, curr_j = i + di, j + dj
                while 0 <= curr_i < n and 0 <= curr_j < n:
                    if grid[curr_i][curr_j] == "Q":
                        return False
                    curr_i += di
                    curr_j += dj

            return True

        def dfs(i):
            if i == n:
                if check_goal(grid):
                    res.append(["".join(row) for row in grid])
                return
            
            for new_pos in range(n):
                if check(grid, i, new_pos):
                    grid[i][new_pos] = "Q"
                    dfs(i+1)
                    grid[i][new_pos] = "."

            return 

        dfs(0)
        return res
