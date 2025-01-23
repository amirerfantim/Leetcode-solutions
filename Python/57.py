from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []

        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)
        res.extend(intervals[i:])

        return res


s1 = Solution()
print(s1.insert([[0,2],[3,9]], [6, 8]))