# 剑指 offer 31.栈的压入、弹出序列
from typing import List


class Solution:
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    #     stack = []
    #     j = 0
    #     for c in pushed:
    #         stack.append(c)
    #         while stack and stack[-1] == popped[j]:
    #             stack.pop()
    #             j += 1
    #     return not stack

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, stack = 0, []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack


s = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(s.validateStackSequences(pushed, popped))

pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
print(s.validateStackSequences(pushed, popped))
