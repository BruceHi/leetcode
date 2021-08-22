from typing import List
import heapq


class Solution:
    # 超时
    # def minStoneSum(self, piles: List[int], k: int) -> int:
    #     for _ in range(k):
    #         i = piles.index(max(piles))
    #         piles[i] -= piles[i] // 2
    #     return sum(piles)

    # 超时
    # def minStoneSum(self, piles: List[int], k: int) -> int:
    #     max_idx = 0
    #     for _ in range(k):
    #         for i, p in enumerate(piles):
    #             if piles[max_idx] < p:
    #                 max_idx = i
    #         piles[max_idx] -= piles[max_idx] // 2
    #     return sum(piles)

    def minStoneSum(self, piles: List[int], k: int) -> int:
        nums = [-x for x in piles]
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heapreplace(nums, nums[0] + (-nums[0]) // 2)  # pop Push
        return -sum(nums)


s = Solution()
piles = [5,4,9]
k = 2
print(s.minStoneSum(piles, k))

piles = [4,3,6,7]
k = 3
print(s.minStoneSum(piles, k))
