import sys
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_points = []
        for point in points:
            if point[0] == x or point[1] == y:
                valid_points.append(point)

        if len(valid_points) == 0:
            return -1
        else:
            distance = sys.maxsize
            result = 0
            for i in range(len(valid_points)):
                cur = abs(valid_points[i][0] - x) + abs(valid_points[i][1] - y)
                if cur < distance:
                    distance = cur
                    result = points.index(valid_points[i])
        return result


s1 = Solution()
a = [[25, 45], [60, 19], [11, 38], [32, 22], [1, 24], [26, 25], [52, 36], [45, 54], [45, 30], [45, 39], [39, 38],
     [25, 38], [39, 57], [47, 51], [47, 49], [37, 21], [16, 43], [53, 33], [10, 50], [30, 29], [3, 31], [45, 26],
     [22, 40], [2, 31], [57, 42], [25, 42], [37, 13], [13, 54], [17, 5], [50, 32]]
print(s1.nearestValidPoint(28, 51, a))
