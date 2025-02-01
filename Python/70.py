class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2]
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])
        return arr[n - 1]


s = Solution()
print(s.climbStairs(4))
