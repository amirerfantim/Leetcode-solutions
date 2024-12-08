class Solution(object):
    def maxArea(self, height):
        maximum_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            if height[left_pointer] < height[right_pointer]:
                maximum_area = max((right_pointer - left_pointer) * (height[left_pointer]), maximum_area)
                left_pointer += 1
            else:
                maximum_area = max((right_pointer - left_pointer) * (height[right_pointer]), maximum_area)
                right_pointer -= 1
        return maximum_area



s1 = Solution()
h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(s1.maxArea(h))
