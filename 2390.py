class Solution(object):
    def removeStars(self, s):
        stack = []
        stack2 = []
        star_counter = 0
        for char in s:
            stack.append(char)
        while len(stack) > 0:
            if stack[-1] == '*':
                star_counter += 1
                stack.pop()
            elif star_counter > 0:
                stack.pop()
                star_counter -= 1
            else:
                stack2 += stack.pop()
        stack2.reverse()
        return "".join(stack2)




