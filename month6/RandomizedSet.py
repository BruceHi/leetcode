# 常数时间插入、删除和获取随机元素
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.size = 0  # len(list) 的时间复杂度也是 O（1），所以不用 size 也可以。
        self.tmp = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data:
            self.data[val] = self.size
            self.tmp.append(val)
            self.size += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            i = self.data.pop(val)
            self.tmp[i] = None
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        a = random.choice(self.tmp)
        while a is None:
            a = random.choice(self.tmp)  # 随机取元素返回。
        return a


# 初始化一个空的集合。
randomSet = RandomizedSet()

#  向集合中插入 1 。返回 true 表示 1 被成功地插入。
print(randomSet.insert(1))

# 返回 false ，表示集合中不存在 2 。
print(randomSet.remove(2))

# 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
print(randomSet.insert(2))

# getRandom 应随机返回 1 或 2 。
print(randomSet.getRandom())

# 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
print(randomSet.remove(1))

# 2 已在集合中，所以返回 false 。
print(randomSet.insert(2))

# 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
print(randomSet.getRandom())
