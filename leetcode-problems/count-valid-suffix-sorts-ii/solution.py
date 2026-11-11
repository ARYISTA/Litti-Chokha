class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> list[int]:
        n, m = len(nums), len(target)
        S = nums + [-1] + target
        z = [0] * len(S)
        l = r = 0
        for i in range(1, len(S)):
            if i <= r: z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < len(S) and S[z[i]] == S[i + z[i]]: z[i] += 1
            if i + z[i] - 1 > r: l, r = i, i + z[i] - 1
                
        prev_bad, last = [-1] * m, -1
        for j in range(1, m):
            if target[j - 1] < target[j]: last = j
            prev_bad[j] = last
        mv = max(max(nums), max(target))
        nf, wf = [0] * (mv + 1), [0] * (mv + 1)
        for x in nums: nf[x] += 1
        for i in range(n): wf[target[i]] += 1
        diff_sum = sum(abs(wf[v] - nf[v]) for v in range(mv + 1))

        ans = []
        for k in range(m - n + 1):
            if k > 0:
                o, i_v = target[k - 1], target[k + n - 1]
                diff_sum += abs(wf[o] - 1 - nf[o]) - abs(wf[o] - nf[o])
                wf[o] -= 1
                diff_sum += abs(wf[i_v] + 1 - nf[i_v]) - abs(wf[i_v] - nf[i_v])
                wf[i_v] += 1

            if diff_sum != 0:
                ans.append(0)
            else:
                first_diff = min(n, z[n + 1 + k])
                b = prev_bad[k + n - 1]
                s_start = max(0, b - k)
                ans.append(max(0, min(n - 1, first_diff) - s_start + 1))
        return ans
























































    