class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        differences = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                differences.append(s1[i])
                differences.append(s2[i])
        if len(differences) == 4 and differences[0] == differences[3] and differences[1] == differences[2]:
            return True
        elif len(differences) == 0:
            return True
        else:
            return False
