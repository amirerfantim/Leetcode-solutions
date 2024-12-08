class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res_word = []
        for i in range(min(len(word1), len(word2))):
            res_word.append(word1[i])
            res_word.append(word2[i])
        res_word.append(word1[i+1:])
        res_word.append(word2[i+1:])
        return "".join(res_word)

s1 = Solution()
word1 = "abc"
word2 = "pqr"
print(s1.mergeAlternately(word1, word2))


