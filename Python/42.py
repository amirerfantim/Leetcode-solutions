from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = height[0]
        right_max = height[-1]
        left = 0
        right = len(height) - 1
        trapped_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                if height[left] > left_max:
                    left_max = height[left]
                trapped_water += left_max - height[left]
            else:
                right -= 1
                if height[right] > right_max:
                    right_max = height[right]
                trapped_water += right_max - height[right]
        return trapped_water

s1 = Solution()
print(s1.trap([3, 0, 3]))
