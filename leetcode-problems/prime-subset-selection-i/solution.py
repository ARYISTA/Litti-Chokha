class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n < 2 or s < 2:
            return []

       
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
                    
        primes = [p for p in range(2, n + 1) if is_prime[p]]

      
        ans = []
        total_sum = 0
        
        for p in primes:
            if total_sum + p <= s:
                ans.append(p)
                total_sum += p
            else:
                break

        return ans