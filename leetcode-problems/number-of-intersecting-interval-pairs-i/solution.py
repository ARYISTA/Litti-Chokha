class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort()
        n = len(intervals)
        count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
               
                if intervals[j][0] <= intervals[i][1]:
                    count += 1
                else:
                    break
                    
        return count