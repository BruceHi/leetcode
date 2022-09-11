# 寻找比目标字母大的最小字母
from typing import List
from bisect import bisect


class Solution:

    # # 若是二分查找的话，时间复杂度是 O(log n)，那么题目就是中等难度的题了
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     left, right = 0, len(letters) - 1
    #     while left < right:
    #         mid = left + right >> 1
    #         if letters[mid] <= target:
    #             left = mid + 1
    #         else:
    #             right = mid
    #
    #     if right == len(letters) - 1:
    #         if letters[-1] > target:
    #             return letters[-1]
    #         return letters[0]
    #     return letters[right]

    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     for c in letters:
    #         if c > target:
    #             return c
    #     return letters[0]

    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     idx = bisect(letters, target)
    #     return letters[idx % len(letters)]

    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     for c in letters:
    #         if c > target:
    #             return c
    #     return letters[0]

    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     left, right = 0, len(letters) - 1
    #     while left < right:
    #         mid = left + right >> 1
    #         if letters[mid] <= target:  # 注意要先排除小于等于的
    #             left = mid + 1
    #         else:
    #             right = mid
    #
    #     if letters[left] <= target:
    #         return letters[0]
    #     return letters[right]

    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     for c in letters:
    #         if c > target:
    #             return c
    #     return letters[0]

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if c > target:
                return c
        return letters[0]


s = Solution()
letters = ["c", "f", "j"]
target = "a"
print(s.nextGreatestLetter(letters, target))

letters = ["c", "f", "j"]
target = "c"
print(s.nextGreatestLetter(letters, target))

letters = ["c", "f", "j"]
target = "d"
print(s.nextGreatestLetter(letters, target))

letters = ["c", "f", "j"]
target = "g"
print(s.nextGreatestLetter(letters, target))

letters = ["c", "f", "j"]
target = "j"
print(s.nextGreatestLetter(letters, target))

letters = ["c", "f", "j"]
target = "k"
print(s.nextGreatestLetter(letters, target))
