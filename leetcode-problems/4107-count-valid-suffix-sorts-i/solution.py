class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        if sorted(nums) != sorted(target):
            return 0
        n = len(nums)
        first_diff = next((i for i in range(n) if nums[i] != target[i]), n)
        s_start = n - 1
        while s_start > 0 and target[s_start - 1] >= target[s_start]:
            s_start -= 1
        return max(0, min(n - 1, first_diff) - s_start + 1)
        