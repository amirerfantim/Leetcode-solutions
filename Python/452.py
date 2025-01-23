from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        end = points[0][1]
        arrows = 1

        for point in points:
            if point[0] > end:
                arrows += 1
                end = point[1]
            elif point[1] < end:
                end = point[1]

        return arrows
