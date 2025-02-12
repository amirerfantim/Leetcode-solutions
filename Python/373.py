from typing import List
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        result = []
        visited = set()
        visited.add((0, 0))
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        while k > 0 and heap:
            _, first_index, second_index = heapq.heappop(heap)
            result.append((nums1[first_index], nums2[second_index]))
            k -= 1

            if first_index + 1 < len(nums1) and (first_index + 1, second_index) not in visited:
                heapq.heappush(heap, (nums1[first_index + 1] + nums2[second_index], first_index + 1, second_index))
                visited.add((first_index + 1, second_index))

            if second_index + 1 < len(nums2) and (first_index, second_index + 1) not in visited:
                heapq.heappush(heap, (nums1[first_index] + nums2[second_index + 1], first_index, second_index + 1))
                visited.add((first_index, second_index + 1))
        return result


s1 = Solution()
print(s1.kSmallestPairs([1, 7, 11], [2, 4, 6], 5))
