class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        l, m, r = 0, 1, 1
        for i in range(n - 2):
            current = l + m + r
            l, m, r = m, r, current

        return r


s1 = Solution()
print(s1.tribonacci(25))
