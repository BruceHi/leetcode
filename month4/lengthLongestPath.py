# 388.文件的最长绝对路径
from collections import defaultdict


class Solution:
    # def lengthLongestPath(self, input: str) -> int:
    #     res = 0
    #     depth_length_map = {-1: 0}
    #     # 按照顺序来的，所以不担心新的路径会覆盖原有的
    #     for line in input.split('\n'):
    #         depth = line.count('\t')
    #         # 每行制表符（空格）最后要被去掉
    #         # 其中 \n 表示一个字符，反斜杠和字符连在一块算一个字符
    #         depth_length_map[depth] = depth_length_map[depth - 1] + len(line) - depth
    #         if line.count('.'):
    #             # 每层都要添加depth个 /
    #             res = max(res, depth_length_map[depth] + depth)
    #     return res

    # def lengthLongestPath(self, input: str) -> int:
    #     res = 0
    #     dic = defaultdict(int)
    #     for line in input.split('\n'):
    #         path = line.count('\t')
    #         dic[path] = dic[path-1] + len(line) - path
    #         if line.count('.'):
    #             res = max(res, dic[path] + path)
    #     return res


    def lengthLongestPath(self, input: str) -> int:
        res = 0
        dic = defaultdict(int)
        for line in input.split('\n'):
            depth = line.count('\t')
            dic[depth] = dic[depth-1] + len(line) - depth
            if line.count('.'):
                res = max(res, dic[depth] + depth)
        return res

s = Solution()
input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(s.lengthLongestPath(input))

input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(s.lengthLongestPath(input))

input = "a"
print(s.lengthLongestPath(input))

input = "file1.txt\nfile2.txt\nlongfile.txt"
print(s.lengthLongestPath(input))
