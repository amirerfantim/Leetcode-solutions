class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        global_max = 0
        curr_max = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i, ch in enumerate(s):
            if i >= k:
                if s[i - k] in vowels:
                    curr_max -= 1
            if ch in vowels:
                curr_max += 1
            global_max = max(curr_max, global_max)
            if global_max == k:
                break

        return global_max
