from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            for i in range(nums2.index(num) + 1, len(nums2)):
                if nums2[i] > num:
                    ans.append(nums2[i])
                    break
            else:
                ans.append(-1)
        return ans


s1 = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(s1.nextGreaterElement(nums1, nums2))
