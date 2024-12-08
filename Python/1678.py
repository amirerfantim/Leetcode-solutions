class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')


s = Solution()
command = "G()(al)"
print(s.interpret(command))