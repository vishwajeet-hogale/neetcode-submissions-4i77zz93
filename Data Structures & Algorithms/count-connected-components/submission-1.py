from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        ad_list = defaultdict(list)
        for i,j in edges:
            ad_list[i].append(j)
            ad_list[j].append(i)

        vis = [0 for _ in range(n)]

        def dfs(i):
            if vis[i] or i >= n:
                return
            vis[i] = 1
            for neigh in ad_list[i]:
                if not vis[neigh]:
                    dfs(neigh)
            return

        c = 0
        for node in range(n):
            if not vis[node]:
                dfs(node)
                c += 1

        return c

        
        