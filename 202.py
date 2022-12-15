class Solution:
    def isHappy(self, n: int) -> bool:
        nums = []
        while True:
            nums.append(n)
            if n == 1:
                return True
            temp = 0
            while n > 0:
                temp += pow(n % 10, 2)
                n = n // 10
            n = temp
            if n in nums:
                return False


s1 = Solution()
print(s1.isHappy(19))