from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            n -= 1
        if len(flowerbed) > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
        if len(flowerbed) > 1 and flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) -2 ] == 0:
            n -= 1
            flowerbed[len(flowerbed) - 1] = 1
        for i in range(1, len(flowerbed) - 1):
            if i == 0 and i + 1 < len(flowerbed):
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1 and i - 1 >= 0:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i] == 1:
                    continue
                if flowerbed[i] == 0 and (flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0):
                    n -= 1
                    flowerbed[i] = 1
        print(flowerbed)
        if n <= 0:
            return True
        else:
            return False


s1 = Solution()
s1.canPlaceFlowers([0, 0, 1, 0, 1], 1)
