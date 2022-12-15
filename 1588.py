from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)

        res = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub_arr = arr[i:j]
                if len(sub_arr) % 2 != 0:
                    res += sum(sub_arr)

        return res




s1 = Solution()
arr = [1, 4, 2, 5, 3]
print(s1.sumOddLengthSubarrays(arr))
