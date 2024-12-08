from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bits = [0 for i in range(len(arr))]
        temp = arr[:]
        for i in range(len(temp)):
            while temp[i] > 0:
                if temp[i] % 2 == 1:
                    bits[i] += 1
                temp[i] = temp[i] // 2
        temp = []
        for x, y in sorted(zip(bits, arr)):
            temp.append(y)
        return temp


s1 = Solution()
arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
print(s1.sortByBits(arr))
