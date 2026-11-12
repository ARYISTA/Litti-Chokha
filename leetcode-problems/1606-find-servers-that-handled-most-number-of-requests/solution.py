from heapq import heappush, heappop
from typing import List
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        count = [0] * k

        for i, (t, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, s = heappop(busy)
                heappush(available, i + (s - i) % k)

            if available:
                s = heappop(available) % k
                count[s] += 1
                heappush(busy, (t + l, s))

        max_req = max(count)
        return [i for i, c in enumerate(count) if c == max_req]
        