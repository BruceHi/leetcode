# 380. O(1) 时间插入、删除和获取随机元素
# 常数时间插入、删除和获取随机元素
from random import choice


# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.data = {}
#         self.size = 0  # len(list) 的时间复杂度也是 O（1），所以不用 size 也可以。
#         self.tmp = []
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.data:
#             self.data[val] = self.size
#             self.tmp.append(val)
#             self.size += 1
#             return True
#         return False
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.data:
#             i = self.data.pop(val)
#             self.tmp[i] = None
#             return True
#         return False
#
#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         a = random.choice(self.tmp)
#         while a is None:
#             a = random.choice(self.tmp)  # 随机取元素返回。
#         return a


# 初始化一个空的集合。

# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.nums = set()
#
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.nums:
#             self.nums.add(val)
#             return True
#         return False
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.nums:
#             self.nums.remove(val)
#             return True
#         return False
#
#     # list() 的时间复杂度是 O(n)，不合题意
#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         # tmp = list(self.nums)
#         # n = len(tmp)
#         # if n > 0:
#         #     return tmp[random.randrange(0, n)]
#
#         if len(self.nums) > 0:
#             return random.choice(list(self.nums))

# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.nums = []
#         self.dic = {}
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val in self.dic:
#             return False
#         self.dic[val] = len(self.nums)  # 顺序不能错了
#         self.nums.append(val)
#         return True
#
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         # 只剩一个值，这样写就不行了。
#         # if val in self.dic:
#         #     i = self.dic.pop(val)
#         #     tmp = self.nums[-1]
#         #     self.dic[tmp] = i
#         #     self.nums[i], self.nums[-1] = tmp, self.nums[i]
#         #     self.nums.pop()
#         #     return True
#         # return False
#
#         if val in self.dic:
#             idx, tmp = self.dic[val], self.nums[-1]
#             self.nums[idx], self.dic[tmp] = tmp, idx
#             self.nums.pop()
#             del self.dic[val]
#             return True
#         return False
#
#     def getRandom(self) -> int:
#         return random.choice(self.nums)

# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.nums = []
#         self.dic = {}
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val in self.dic:
#             return False
#         self.dic[val] = len(self.nums)  # 顺序不能错了
#         self.nums.append(val)
#         return True
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val in self.dic:
#             i = self.dic.pop(val)
#             self.nums[i] = None
#             return True
#         return False
#
#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         a = random.choice(self.nums)
#         while a is None:
#             a = random.choice(self.nums)  # 随机取元素返回。
#         return a

# class RandomizedSet:
#
#     def __init__(self):
#         self.nums = set()
#
#     def insert(self, val: int) -> bool:
#         if val not in self.nums:
#             self.nums.add(val)
#             return True
#         return False
#
#     def remove(self, val: int) -> bool:
#         if val in self.nums:
#             self.nums.remove(val)
#             return True
#         return False
#
#     def getRandom(self) -> int:
#         return random.choice(list(self.nums))


# class RandomizedSet:
#
#     def __init__(self):
#         self.nums = []
#         self.dic = {}
#
#
#     def insert(self, val: int) -> bool:
#         if val not in self.nums:
#             self.dic[val] = len(self.nums)
#             self.nums.append(val)
#             return True
#         return False
#
#
#     def remove(self, val: int) -> bool:
#         if val in self.nums:
#             i = self.dic.pop(val)
#             self.nums[i] = None
#             return True
#         return False
#
#
#     def getRandom(self) -> int:
#         a = random.choice(self.nums)
#         while a is None:
#             a = random.choice(self.nums)
#         return a

# 官方解答
# class RandomizedSet:
#
#     def __init__(self):
#         self.nums = []
#         self.dic = {}
#
#     def insert(self, val: int) -> bool:
#         if val in self.dic:
#             return False
#         self.dic[val] = len(self.nums)
#         self.nums.append(val)
#         return True
#
#     # 在remove的时候，用list末尾的那个元素替换移除的元素
#     # def remove(self, val: int) -> bool:
#     #     if val not in self.nums:  # 注意，若这里换成 self.dic 是错误的，还需要考虑只有一个元素的情况，下面没有考虑，是错误的
#     #         return False
#     #     i = self.dic.pop(val)
#     #     self.nums[i] = self.nums[-1]
#     #     self.dic[self.nums[-1]] = i
#     #     self.nums.pop()
#     #     return True
#
#     def remove(self, val: int) -> bool:
#         if val not in self.dic:
#             return False
#         i = self.dic[val]
#         self.nums[i] = self.nums[-1]
#         self.dic[self.nums[-1]] = i
#         self.dic.pop(val)
#         self.nums.pop()
#         return True
#
#     def getRandom(self) -> int:
#         return random.choice(self.nums)


# randomSet = RandomizedSet()
# #  向集合中插入 1 。返回 true 表示 1 被成功地插入。
# print(randomSet.insert(1))
# # 返回 false ，表示集合中不存在 2 。
# print(randomSet.remove(2))
# # 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# print(randomSet.insert(2))
#
# # getRandom 应随机返回 1 或 2 。
# print(randomSet.getRandom())
#
# # 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# print(randomSet.remove(1))
#
# # 2 已在集合中，所以返回 false 。
# print(randomSet.insert(2))
#
# # 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
# print(randomSet.getRandom())
#
# print('---------------')
#
# randomSet = RandomizedSet()
#
# print(randomSet.remove(0))
# print(randomSet.remove(0))
# print(randomSet.insert(0))
# print(randomSet.getRandom())
# print(randomSet.remove(0))
# print(randomSet.insert(0))


# ---- 测试 ----


# def print_result(funs, paras):
#     res = []
#     obj = None
#     for i, (f, p) in enumerate(zip(funs, paras)):
#         if i == 0:
#             res.append(obj)
#             obj = eval(f)(*p)
#         else:
#             res.append(getattr(obj, f)(*p))
#     print(res)

# class RandomizedSet:
#
#     def __init__(self):
#         self.nums = []
#         self.dic = {}
#
#     def insert(self, val: int) -> bool:
#         if val in self.dic:
#             return False
#         self.dic[val] = len(self.nums)
#         self.nums.append(val)
#         return True
#
#     def remove(self, val: int) -> bool:
#         if val not in self.dic:
#             return False
#         idx = self.dic[val]
#         last = self.nums[-1]
#
#         self.nums[idx] = last
#         self.nums.pop()
#
#         self.dic[last] = idx
#         del self.dic[val]
#         return True
#
#     def getRandom(self) -> int:
#         return choice(self.nums)

# class RandomizedSet:
#
#     def __init__(self):
#         self.nums = []
#         self.dic = {}
#
#
#     def insert(self, val: int) -> bool:
#         if val in self.dic:
#             return False
#         self.dic[val] = len(self.nums)
#         self.nums.append(val)
#         return True
#
#
#     def remove(self, val: int) -> bool:
#         if val not in self.dic:
#             return False
#
#         idx = self.dic[val]
#         last = self.nums[-1]
#
#         self.nums[idx] = last
#         self.nums.pop()
#
#         self.dic[last] = idx
#         del self.dic[val]
#
#         return True
#
#     def getRandom(self) -> int:
#         return choice(self.nums)

# class RandomizedSet:
#
#     def __init__(self):
#         self.dic = {}
#         self.nums = []
#
#
#     def insert(self, val: int) -> bool:
#         if val in self.dic:
#             return False
#         self.dic[val] = len(self.nums)
#         self.nums.append(val)
#         return True
#
#
#     def remove(self, val: int) -> bool:
#         if val not in self.dic:
#             return False
#
#         idx = self.dic[val]
#         last = self.nums[-1]
#
#         self.nums[idx] = last
#         self.nums.pop()
#
#         self.dic[last] = idx
#         del self.dic[val]
#         return True
#
#     def getRandom(self) -> int:
#         return choice(self.nums)


class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False

        num = self.nums[-1]
        idx = self.dic[val]

        self.dic[num] = idx
        self.dic.pop(val)

        self.nums[idx] = num
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return choice(self.nums)


def print_result(funs, paras):
    res = [None]
    obj = eval(funs[0])(*paras[0])
    for f, p in zip(funs[1:], paras[1:]):
        res.append(getattr(obj, f)(*p))
    print(res)


t = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
s = [[], [1], [2], [2], [], [1], [2], []]
print_result(t, s)

t = ["RandomizedSet", "remove", "remove", "insert", "getRandom", "remove", "insert"]
s = [[], [0], [0], [0], [], [0], [0]]
print_result(t, s)
