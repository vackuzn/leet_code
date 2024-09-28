class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 1:
            return intervals

        intervals_sorted = sorted(intervals, key=lambda i:i[0])

        idx = 0
        while idx < len(intervals_sorted) - 1:
            cur_start, cur_end = intervals_sorted[idx]
            next_start, next_end = intervals_sorted[idx + 1]

            if next_start <= cur_end:
                intervals_sorted[idx] = [cur_start, max(cur_end, next_end)]
                del intervals_sorted[idx + 1]
            else:
                idx += 1
        
        return intervals_sorted


intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,3],[8,10],[2,6],[15,18]]
print(Solution().merge(intervals))

# sort intervals by start
# for each interval check if next interval has start within current [a,b] - update end for max(end_itv_1,end_itv_2)
# if next interval starts after current end - use next as current and repeat
# if no intervals left - finish