class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights), len(heights[0])
        at = [["" for _ in range(m)] for _ in range(n)]
        pc = [["" for _ in range(m)] for _ in range(n)]

        def dfs(vis, i, j, n, m, oc = "A"):
            if i < 0 or i >= n or j < 0 or j >= m or vis[i][j] != "":
                return
            vis[i][j] = oc
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            for x,y in directions:
                nx, ny = i + x, j + y
                if 0 <= nx < n and 0 <= ny < m and vis[nx][ny]=="" and heights[i][j] <= heights[nx][ny]:
                    dfs(vis, nx, ny, n, m, oc)
            return

        # Atlantic
        for i in range(n):
            dfs(at, i, m-1, n, m, "A")
        for j in range(m):
            dfs(at, n-1, j, n, m, "A")

        # Pacific
        for i in range(n):
            dfs(pc, i, 0, n, m, "P")
        for j in range(m):
            dfs(pc, 0, j, n, m, "P")
        # Check what reached to both
        res = []
        for i in range(n):
            for j in range(m):
                if at[i][j] == "A" and pc[i][j] == "P":
                    res.append([i,j])

        return res



