class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        b_current_idx = len(b) - 1
        a_current_idx = len(a) - 1
        result = []

        while a_current_idx >= 0 or b_current_idx >= 0 or carry:
            a_value = int(a[a_current_idx]) if a_current_idx >= 0 else 0
            b_value = int(b[b_current_idx]) if b_current_idx >= 0 else 0
            current = a_value + b_value + carry
            result.append(str(current % 2))
            carry = current // 2
            a_current_idx -= 1
            b_current_idx -= 1

        return ''.join(reversed(result))


s1 = Solution()
print(s1.addBinary("11", "1"))