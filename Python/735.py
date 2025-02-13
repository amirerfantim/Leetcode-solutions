from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if -a > stack[-1]:
                    stack.pop()
                elif -a == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)

        return stack


s1 = Solution()
print(s1.asteroidCollision([-9, 5, -7, 5, 2, -5, -5, 8, 3, 10]))
