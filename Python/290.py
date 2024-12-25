class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_map = {}
        words = s.split()
        chars_num = len(pattern)

        if len(words) != chars_num:
            return False

        for index in range(chars_num):
            if pattern[index] not in pattern_map.keys():
                if words[index] in pattern_map.values():
                    return False
                pattern_map[pattern[index]] = words[index]
            else:
                if pattern_map[pattern[index]] != words[index]:
                    return False
        return True


s1 = Solution()
print(s1.wordPattern("aaaa", "dog cat cat fish"))
