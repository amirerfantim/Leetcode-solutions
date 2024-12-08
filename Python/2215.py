class Solution(object):
    def findDifference(self, nums1, nums2):
        first = 0
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        while first < len(nums1):
            try:
                index = nums2.index(nums1[first])
                del nums1[first]
                del nums2[index]
            except ValueError:
                first += 1
                continue
        return nums1, nums2


s1 = Solution()
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
s1.findDifference(nums1, nums2)
