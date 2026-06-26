class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        num_components = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                num_components += 1

        return num_components
