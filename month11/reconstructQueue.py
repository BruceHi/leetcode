# 根据身高重建队列
from typing import List


# 还是有些不明白，以后多看看。
class Solution:
    # 由身高高到低排序，k 值由小到大排序。
    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    #     people.sort(key=lambda x: (-x[0], x[1]))
    #     n = len(people)
    #     # ans = list()
    #     ans = []
    #     for person in people:
    #         # ans[person[1]:person[1]] = [person]
    #         ans.insert(person[1], person)
    #     return ans

    # def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    #     people.sort(key=lambda x: (-x[0], x[1]))
    #     print(people)
    #     res = []
    #     for p in people:
    #         res.insert(p[1], p)
    #     return res

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


s = Solution()
nums = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(nums))
