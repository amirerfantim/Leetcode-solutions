from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            l, r = False, False
            if flowerbed[i]:
                continue
            if i - 1 < 0 or not flowerbed[i - 1]:
                l = True
            if i + 1 >= len(flowerbed) or not flowerbed[i + 1]:
                r = True
            if r and l:
                n -= 1
                flowerbed[i] = 1
            if n <= 0:
                return True
        return not bool(n)


s1 = Solution()
print(s1.canPlaceFlowers([1], 0))
