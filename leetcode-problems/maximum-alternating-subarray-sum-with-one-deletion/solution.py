class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        INF = float('inf')

        # ---------------------------------------------------------
        # 1. Left-to-Right (Prefix) DP
        # L_even[i]: max alt sum of subarray ending at i (element is +)
        # L_odd[i]:  max alt sum of subarray ending at i (element is -)
        # ---------------------------------------------------------
        L_even = [-INF] * n
        L_odd = [-INF] * n

        even, odd = -INF, -INF
        max_no_del = -INF

        for i in range(n):
            x = nums[i]
            prev_even, prev_odd = even, odd
            
            even = max(x, prev_odd + x if prev_odd != -INF else -INF)
            odd = prev_even - x if prev_even != -INF else -INF
            
            L_even[i] = even
            L_odd[i] = odd
            max_no_del = max(max_no_del, even, odd)

        # ---------------------------------------------------------
        # 2. Right-to-Left (Suffix) DP
        # R_start_plus[i]:  max alt sum starting at i, where nums[i] is (+)
        # R_start_minus[i]: max alt sum starting at i, where nums[i] is (-)
        # ---------------------------------------------------------
        R_start_plus = [-INF] * n
        R_start_minus = [-INF] * n

        r_plus, r_minus = -INF, -INF

        for i in range(n - 1, -1, -1):
            x = nums[i]
            prev_plus, prev_minus = r_plus, r_minus

            # If this element is (+), it extends a suffix that expects a (-) next
            r_plus = max(x, x + prev_minus if prev_minus != -INF else -INF)
            
            # If this element is (-), it extends a suffix that expects a (+) next
            r_minus = max(-x, -x + prev_plus if prev_plus != -INF else -INF)

            R_start_plus[i] = r_plus
            R_start_minus[i] = r_minus

        # CRITICAL FIX: Standalone right-side subarrays MUST start with a (+) sign.
        # Therefore, R_max_suff only aggregates R_start_plus values.
        R_max_suff = [-INF] * n
        curr_max = -INF
        for i in range(n - 1, -1, -1):
            curr_max = max(curr_max, R_start_plus[i])
            R_max_suff[i] = curr_max

        # ---------------------------------------------------------
        # 3. Try deleting each element nums[i]
        # ---------------------------------------------------------
        max_with_del = -INF

        for i in range(n):
            # Case A: Delete nums[i], pick subarray ONLY from LEFT (0 to i-1)
            if i > 0:
                max_with_del = max(max_with_del, L_even[i - 1], L_odd[i - 1])

            # Case B: Delete nums[i], pick subarray ONLY from RIGHT (i+1 to n-1)
            if i < n - 1:
                max_with_del = max(max_with_del, R_max_suff[i + 1])

            # Case C: Delete nums[i] and STITCH left and right subarrays together
            if i > 0 and i < n - 1:
                # Left ends at (+), Right must start at (-)
                if L_even[i - 1] != -INF and R_start_minus[i + 1] != -INF:
                    max_with_del = max(max_with_del, L_even[i - 1] + R_start_minus[i + 1])

                # Left ends at (-), Right must start at (+)
                if L_odd[i - 1] != -INF and R_start_plus[i + 1] != -INF:
                    max_with_del = max(max_with_del, L_odd[i - 1] + R_start_plus[i + 1])

        return max(max_no_del, max_with_del)