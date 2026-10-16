class Solution:
    def minRotations(self, n: int, s: str) -> int:
        def cost(a: int, b: int) -> int:
            diff = abs(a - b)
            return min(diff, 10 - diff)

        digits = [int(c) for c in s]

        
        suff_cost = [0] * n
        for i in range(n - 2, -1, -1):
            suff_cost[i] = suff_cost[i + 1] + cost(digits[i], digits[i + 1])

        
        normal_cost = cost(0, digits[0])
        for i in range(n - 1):
            normal_cost += cost(digits[i], digits[i + 1])
        
        min_total_cost = normal_cost

        
        prefix_cost = 0
        current_pos = 0

        for k in range(n):
            
            jump_cost = cost(current_pos, digits[-1])
            
            
            internal_suffix_cost = suff_cost[k]
            
            total_k_cost = prefix_cost + jump_cost + internal_suffix_cost
            min_total_cost = min(min_total_cost, total_k_cost)

            
            prefix_cost += cost(current_pos, digits[k])
            current_pos = digits[k]

        return min_total_cost