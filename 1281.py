class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        for i in str(n):
            s += int(i)
            p *= int(i)
        return p-s


s1 = Solution()
print(s1.subtractProductAndSum(234))
