# 71. 简化路径
import os


class Solution:
    # def simplifyPath(self, path: str) -> str:
    #     paths = path.split('/')
    #     stack = []
    #     for path in paths:
    #         if not path or path == '.':
    #             continue
    #         if path == '..':
    #             if stack:
    #                 stack.pop()
    #             else:
    #                 continue
    #         else:
    #             stack.append(path)
    #     return '/'+'/'.join(stack)

    #
    # def simplifyPath(self, path: str) -> str:
    #     stack = []
    #     for path in path.split('/'):
    #         if path not in ['', '.', '..']:
    #             stack.append(path)
    #         elif path == '..' and stack:
    #             stack.pop()
    #     return '/' + '/'.join(stack)

    # def simplifyPath(self, path: str) -> str:
    #     stack = []
    #     for p in path.split('/'):
    #         if p not in ['', '.', '..']:
    #             stack.append(p)
    #         elif p == '..' and stack:
    #             stack.pop()
    #     return '/' + '/'.join(stack)

    def simplifyPath(self, path: str) -> str:
        return os.path.realpath(path)


s = Solution()
path = "/home/"
print(s.simplifyPath(path))

path = "../../"
print(s.simplifyPath(path))

path = "/home//foo/"
print(s.simplifyPath(path))

path = "/a/./b/../../c/"
print(s.simplifyPath(path))

# path = "/home/"
# print(s.simplifyPath(path))
