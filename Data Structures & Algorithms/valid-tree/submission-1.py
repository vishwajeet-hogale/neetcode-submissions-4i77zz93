from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for nei in g[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True

        # start from 0 (or any node)
        if not dfs(0, -1):
            return False

        # must be connected
        return len(visited) == n