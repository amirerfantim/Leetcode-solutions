from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != arr[1] - arr[0]:
                return False
        return True
