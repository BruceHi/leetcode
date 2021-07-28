from typing import List
from itertools import permutations

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        def compat(stu, men):
            res = 0
            for a, b in zip(stu,men):
                res += (a == b)
            return res

        # nums = permutations(mentors)
        # print(list(permutations(mentors)))
        # print(len(list(permutations(mentors))))
        #
        # print(list(nums))   # 迭代器迭代之后再取值就是 0 了
        # print(len(list(nums)))

        res = 0
        for x in permutations(mentors):
            tmp = 0
            for a, b in zip(students, x):
                tmp += compat(a, b)
            res = max(res, tmp)
        return res


s = Solution()
students = [[1,1,0],[1,0,1],[0,0,1]]
mentors = [[1,0,0],[0,0,1],[1,1,0]]
print(s.maxCompatibilitySum(students, mentors))

students = [[0,0],[0,0],[0,0]]
mentors = [[1,1],[1,1],[1,1]]
print(s.maxCompatibilitySum(students, mentors))
