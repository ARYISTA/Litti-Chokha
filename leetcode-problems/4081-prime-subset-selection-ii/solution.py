class Solution:
    def maxPrimeSubset(self, n: int, s: int) -> list[int]:
        if n < 2 or s < 2:
            return []

        
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        primes = [p for p in range(2, n + 1) if is_prime[p]]

        if not primes or primes[0] > s:
            return []

        
        dp = {0: (0, [])}

        for p in primes:
            
            for curr_sum in range(s - p, -1, -1):
                if curr_sum in dp:
                    new_sum = curr_sum + p
                    new_count = dp[curr_sum][0] + 1
                    new_subset = dp[curr_sum][1] + [p]

                    if new_sum not in dp:
                        dp[new_sum] = (new_count, new_subset)
                    else:
                        existing_count, existing_subset = dp[new_sum]
                        
                        
                        if new_count < existing_count:
                            dp[new_sum] = (new_count, new_subset)
                       
                        elif new_count == existing_count:
                            if new_subset < existing_subset:
                                dp[new_sum] = (new_count, new_subset)

        
        max_sum = max(dp.keys())
        if max_sum == 0:
            return []

        return dp[max_sum][1]