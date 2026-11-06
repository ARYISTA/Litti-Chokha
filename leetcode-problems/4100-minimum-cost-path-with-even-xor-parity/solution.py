class Solution:
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v, c in edges:
            adj[u].append((v, c))
            adj[v].append((u, c))

        val_parity = [bin(x).count('1') % 2 for x in values]

        nodes_order = []
        parent = [-1] * n
        stack = [0]
        
        while stack:
            u = stack.pop()
            nodes_order.append(u)
            for v, c in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    stack.append(v)

        INF = float('inf')
        ans = INF
        dp = [[INF, INF] for _ in range(n)]

        for u in reversed(nodes_order):
            u_par = val_parity[u]
            dp[u][u_par] = 0

            for v, c in adj[u]:
                if v == parent[u]: continue

                for p1 in (0, 1):
                    if dp[v][p1] == INF: continue
                    c1 = dp[v][p1] + c
                    for p2 in (0, 1):
                        if dp[u][p2] == INF: continue
                        if (p1 ^ p2) == 0:
                            if c1 + dp[u][p2] < ans:
                                ans = c1 + dp[u][p2]

                for p1 in (0, 1):
                    if dp[v][p1] != INF:
                        c1 = dp[v][p1] + c
                        nxt_p = p1 ^ u_par
                        if c1 < dp[u][nxt_p]:
                            dp[u][nxt_p] = c1

        return ans if ans != INF else -1