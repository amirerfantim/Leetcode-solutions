from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for first, second in zip(words, words[1:]):
            if len(first) < len(second):
                first += '0'
            else:
                second += '0'
            for character_first, character_second in zip(first, second):
                if order.find(character_first) > order.find(character_second):
                    return False
                elif order.find(character_first) < order.find(character_second):
                    break
        return True


s1 = Solution()
words = ["app","apple"]
order = "abcdefghijklmnopqrstuvwxyz"
print(s1.isAlienSorted(words, order))






