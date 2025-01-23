class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')' or char == ']' or char == '}' or char == '}':
                if stack:
                    popped_element = stack.pop()
                    if char == ")" and popped_element != '(':
                        return False
                    if char == "]" and popped_element != '[':
                        return False
                    if char == "}" and popped_element != '{':
                        return False
                else:
                    return False
        return len(stack) == 0


