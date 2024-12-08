from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]

        if coordinates[1][1] == y1:
            for x, y in coordinates[2:]:
                if y != y1:
                    return False
            return True
        m = (coordinates[1][0] - coordinates[0][0]) / (coordinates[1][1] - coordinates[0][1])
        for x, y in coordinates[1:]:
            if y == y1: return False
            if (x - x1) / (y - y1) != m:
                return False
        return True


s1 = Solution()
coordinates = [[21,14],[8,14],[7,14],[17,14],[-10,14],[-8,14],[10,14],[-7,14],[-4,14],[16,14],[-21,14],[-16,14],[2,14],[-15,14],[20,14],[6,14]]
print(s1.checkStraightLine(coordinates))
