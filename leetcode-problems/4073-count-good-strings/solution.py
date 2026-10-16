class Solution:
    def countGoodStrings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 0:
            return 0

        # Helper function to multiply two 2x2 matrices under modulo
        def matrix_mult(A, B):
            return [
                [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
                [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
            ]

        # Helper function to raise a 2x2 matrix to the power of p
        def matrix_pow(A, p):
            res = [[1, 0], [0, 1]]  # Identity matrix
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = matrix_mult(res, base)
                base = matrix_mult(base, base)
                p //= 2
            return res

        # Standard transition matrix for the Fibonacci sequence
        T = [[1, 1], [1, 0]]
        
        # Compute T^(n-1) to find the n-th Fibonacci number
        T_pow = matrix_pow(T, n - 1)
        
        # F_1 = 1, F_2 = 1. The n-th Fibonacci number F_n is located at T_pow[0][0]
        fn = T_pow[0][0]

        # Total strings = 2 * F_n (since the sequence can start with either 'a' or 'b')
        return (2 * fn) % MOD