# 1518. 换酒问题
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res, total = numBottles, numBottles
        while total >= numExchange:
            remain = total // numExchange
            res += remain
            total = remain + total - remain * numExchange
        return res


s = Solution()
numBottles = 9
numExchange = 3
print(s.numWaterBottles(numBottles, numExchange))

numBottles = 15
numExchange = 4
print(s.numWaterBottles(numBottles, numExchange))

numBottles = 5
numExchange = 5
print(s.numWaterBottles(numBottles, numExchange))

numBottles = 2
numExchange = 3
print(s.numWaterBottles(numBottles, numExchange))

numBottles = 15
numExchange = 8
print(s.numWaterBottles(numBottles, numExchange))
