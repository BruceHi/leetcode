import random

# 拒绝采样
# (randX() - 1)*Y + randY() 可以等概率的生成[1, X * Y]范围的随机数
class Solution:
    def rand10(self):
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return num % 10 + 1


def rand7():
    return random.Random()
