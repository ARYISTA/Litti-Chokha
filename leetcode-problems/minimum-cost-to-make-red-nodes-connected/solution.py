from typing import List

class Solution:
    def minCost(self, n: int, colors: str, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        order = [0] * n
        parent = [-1] * n
        parent[0] = 0
        head, tail = 0, 1

        while head < tail:
            u = order[head]
            head += 1
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    order[tail] = v
                    tail += 1
        parent[0] = -1

        sz = [1] * n
        AllBlue = [0] * n
        dp = [0] * n

        for u in reversed(order):
            if colors[u] == 'R':
                AllBlue[u] += sz[u]
            else:
                dp[u] += sz[u]

            p = parent[u]
            if p != -1:
                sz[p] += sz[u]
                abu = AllBlue[u]
                dpu = dp[u]
                AllBlue[p] += abu
                dp[p] += abu if abu < dpu else dpu

        ab0 = AllBlue[0]
        ans = ab0
        for r in range(n):
            c = ab0 - AllBlue[r] + dp[r]
            if c < ans:
                ans = c

        return ans