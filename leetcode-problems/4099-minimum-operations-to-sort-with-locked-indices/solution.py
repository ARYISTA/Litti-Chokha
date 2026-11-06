class Solution:
    def minOperations(self, nums: list[int], locked: list[int], k: int) -> int:
        n = len(nums)
        unlocks = 0
        
        for i in range(n):
            if locked[i] and nums[i] != i + 1:
                locked[i] = 0
                unlocks += 1
                
        rem_k = k - unlocks
        if rem_k < 0: return -1
        
        pref_mx = 0
        for i in range(n):
            if nums[i] > pref_mx:
                pref_mx = nums[i]
            if locked[i] and pref_mx > i + 1:
                if rem_k > 0:
                    locked[i] = 0
                    rem_k -= 1
                    unlocks += 1
                else:
                    return -1

        swaps = 0
        start = 0
        for i in range(n + 1):
            if i == n or locked[i]:
                min_v, max_v = n + 1, 0
                for j in range(start, i):
                    val = nums[j]
                    if val < min_v: min_v = val
                    if val > max_v: max_v = val
                    for m in range(j + 1, i):
                        if val > nums[m]:
                            swaps += 1
                if start < i and (min_v != start + 1 or max_v != i):
                    return -1
                start = i + 1

        return unlocks + swaps