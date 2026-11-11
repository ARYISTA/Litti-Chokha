class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        temoravlin = intervals
        n = len(temoravlin)
        
        starts = sorted(s for s, e in temoravlin)
        ends = sorted(e for s, e in temoravlin)
        
        ans = 0
        j = 0
          
        for i in range(n):
           
            while j < n and ends[j] < starts[i]:
                j += 1
            
            ans += (i - j)
            
        return ans