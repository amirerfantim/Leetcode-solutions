class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        stack = []

        for directory in directories:
            if directory == '' or directory == '.':
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        return '/' + '/'.join(stack)


s = Solution()
print(s.simplifyPath('/home//foo/bar'))