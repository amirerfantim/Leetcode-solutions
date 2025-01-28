from collections import defaultdict
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter_dict = defaultdict(int)
        for num in nums:
            counter_dict[num] += 1
            if counter_dict[num] > 1:
                return True
        return False


s1 = Solution()
nums = [1, 1, 3, 4]
print(s1.containsDuplicate(nums))
