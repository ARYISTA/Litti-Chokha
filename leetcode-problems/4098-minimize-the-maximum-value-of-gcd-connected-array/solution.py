import math

class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:
        if value == 1:
            return -1

        def spf(x):
            if x % 2 == 0: return 2
            for i in range(3, int(math.isqrt(x)) + 1, 2):
                if x % i == 0: return i
            return x

        if index > 0:
            if value % 2 == 0:
                if value - 2 * index <= 0:
                    return -1
            else:
                p = spf(value)
                if value - p <= 0 or (value - p) - 2 * (index - 1) <= 0:
                    return -1

        rem = n - 1 - index
        if rem == 0:
            return value

        if value % 2 == 0:
            return value + 2 * rem
        
        p = spf(value)
        return value + p + 2 * (rem - 1)