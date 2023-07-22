class Solution(object):
    def predictPartyVictory(self, senate):
        senate_queue = [char for char in senate]
        dominated_flag = False

        while not dominated_flag:
            cur = senate_queue[0]
            del senate_queue[0]
            senate_queue.append(cur)
            if cur == 'R':
                try:
                    senate_queue.remove('D')
                except:
                    return "Radiant"
            if cur == 'D':
                try:
                    senate_queue.remove('R')
                except:
                    return "Dire"


s1 = Solution()
senate = "D"
print(s1.predictPartyVictory(senate))