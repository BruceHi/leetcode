def max_lists(*lst):
    return max(max(lst, key=lambda v: max(v)))  # [4, 5, 11] --> 11


# 对于内层 max 的解释： max 要返回一个结果，比较标准是：比较每个元素的最大值。
r = max_lists([1, 2, 9], [6, 7], [4, 5, 11])
print(r)

# a = 3
# b = a
# a = 4
# print(b)

a = [1, 2, 3]
print([-x for x in a])

b = [1, 3, 2]
print(sorted(a) == sorted(b))

a = (1, 2, 3)
b = (3, 2, 1)
print(a == b)

from collections import Counter
a = (1, 2, 3)
print(Counter(a))

res = ((1, 2, 3), (2, 3, 4))
print(list(map(list, res)))

s = [1, 2, 3, 4, 6]
print(s[:-2])

print(-3//2)
print(-3 >> 1)


# import heapq
# s = []
# print(heapq.nsmallest(3, s))
# a = (1, 3, 9, 0)
# heapq.heapify(a)

print([3]+[])
b = set()
b.add(1)
print(b)

c = []
print(len(c))
c.append(4)
print(c)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)


b |= {1}
print()
print(b)

from collections import defaultdict
nums_times = defaultdict(lambda: 'a')
print(nums_times['w'])
print('hello')


from collections import defaultdict

d = defaultdict(dict)
print(d)

b = d['c']
c = d['e']
# print(b)
print(d)

s = ['']
if not s:
    print('ha')
if not s[0]:
    print('d')

# s = set()
a = [{i} for i in range(4)]
print(a)

b = {1}
print(type(b))
