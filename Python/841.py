from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        explored = set()

        while len(stack) > 0:
            cur = stack.pop()
            cur_rooms = rooms[cur]
            explored.add(cur)
            for room in cur_rooms:
                if room not in explored:
                    stack.append(room)

        return len(explored) == len(rooms)


s1 = Solution()
rooms = [[1,2],[2,1],[1]]
print(s1.canVisitAllRooms(rooms))
