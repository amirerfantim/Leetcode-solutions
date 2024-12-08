from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        counter1 = 0
        counter2 = 0
        while True:
            if counter2 >= n or counter1 >= len(nums1):
                break
            if nums2[counter2] < nums1[counter1]:
                for i in range(m, counter1, -1):
                    nums1[i] = nums1[i - 1]
                nums1[counter1] = nums2[counter2]
                m += 1
                counter2 += 1
            if counter1 >= m:
                nums1[counter1] = nums2[counter2]
                counter2 += 1
                m += 1
            counter1 += 1
