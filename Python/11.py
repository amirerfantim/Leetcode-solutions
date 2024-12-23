from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            if current_area > max_area:
                max_area = current_area
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        return max_area


s1 = Solution()
h = [1, 1]
print(s1.maxArea(h))
