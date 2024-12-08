class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        words = s.split()
        r_words = words[::-1]
        res = ""

        for i in range(len(r_words)):
            res += r_words[i]
            if i != len(r_words) - 1:
                res += " "
        return res

s1 = Solution()
s = "the sky is blue"
s1.reverseWords(s)