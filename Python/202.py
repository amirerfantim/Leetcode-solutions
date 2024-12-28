class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()

        def get_next_num(num):
            next_num = 0
            while num:
                digit = num % 10
                num = num // 10
                next_num += digit * digit
            return next_num

        while n != 1:
            if n in nums:
                return False
            nums.add(n)
            n = get_next_num(n)
        return n == 1


s1 = Solution()
print(s1.isHappy(4))