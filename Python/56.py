from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        index = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        while index < len(intervals) - 1:
            if intervals[index + 1][0] <= intervals[index][1]:
                intervals[index][1] = max(intervals[index + 1][1], intervals[index][1])
                del intervals[index + 1]
            else:
                index += 1
        return intervals


s1 = Solution()
print(s1.merge([[2,3],[5,5],[2,2],[3,4],[3,4]]))
