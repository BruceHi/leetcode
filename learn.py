from collections import Counter


def find_duplixate(nums):
    count = Counter(nums)
    return [x for x in count if count[x] > 1]


print(find_duplixate([1, 2, 3, 4, 3, 2]))


def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(5)))


# 返回出现次数最多的元素
def most(nums):
    if not nums:
        return
    return max(nums, key=lambda x: nums.count(x))


print(most([1, 3, 3, 3, 2, 4, 4, 2]))


def most_n(nums):
    if not nums:
        return
    count = Counter(nums)
    return [x for x in count if count[x] == max(count.values())]


print(most_n([1, 3, 3, 3, 2, 4, 4, 4, 2]))


def max_len(*nums):
    return max(*nums, key=lambda x: len(x))


print(max_len([1, 2, 3], [2, 3, 4, 5], [1, 2]))


# 元素对
def pair(nums):
    return list(zip(nums[:-1], nums[1:]))


print(pair([1, 2, 3]))
print(pair(range(10)))

# 样本抽样
from random import randint, sample


nums = [randint(0,50) for _ in range(100)]
print(nums[:5])
print(sample(nums, 10))

print({}.fromkeys(['k1', 'k2', 'k3'], [1, 2, 3]))

print({3: 4}.fromkeys([1, 2], [3]))

a = {1, 2, 3, 4}
b = {2, 3}
print(a.issubset(b))
print(b.issubset(a))


from collections import deque
a = None
b = None
d = deque([a, b])
print(d)
