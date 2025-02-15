from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check_is_possible(k):
            res = 0
            for pile in piles:
                res += ((pile + k - 1) // k)
            if res <= h:
                return True

        r = max(piles)
        l = 1
        while l <= r:
            k = (l + r) // 2
            if check_is_possible(k):
                r = k - 1
            else:
                l = k + 1
        return l


s1 = Solution()
print(s1.minEatingSpeed([312884470], 968709470))