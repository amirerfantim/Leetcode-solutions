from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token.startswith('-') and token.lstrip('-').isdigit():
                stack.append(-int(token[1:]))
            else:
                number2 = stack.pop()
                number1 = stack.pop()
                if token == '+':
                    stack.append(number1 + number2)
                elif token == '-':
                    stack.append(number1 - number2)
                elif token == '*':
                    stack.append(number1 * number2)
                elif token == '/':
                    stack.append(int(number1 / number2))

        return stack[0]


s1 = Solution()
print(s1.evalRPN(["3","-4","+"]))