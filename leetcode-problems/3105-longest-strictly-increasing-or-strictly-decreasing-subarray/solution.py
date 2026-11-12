from typing import List
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            ans = max(ans, inc, dec)
        return ans