import bisect

a = []
index = bisect.bisect_right(a, 1)  # 当 a 式空元素时，bisect_left 和 bisect_right 都返回 0
print(index)

a = [3, 4, 5]
index = bisect.bisect_left(a, 3.5)
print(index)

index = bisect.bisect_right(a, 4)
print(index)

index = bisect.bisect(a, 4)
print(index)

print('ha')
b = {4: [1]}
print(b[4][0])

nums = [1, 2, 4]
mid = 5
start = 0
cnt = 0
for i in range(len(nums)):
    while nums[i] - nums[start] > mid:
        start += 1
    cnt += i - start

print(cnt)

print(ord('('))
print(ord(')'))

print(ord('['))
print(ord(']'))

print(ord('{'))
print(ord('}'))

b = ['  +13']
print(int(*b))

c = []

print(int(*c))


a = {}
b = dict.fromkeys([1, 2], ['q', 'd'])
print(b)
print(a)

a = {1: '2', 2: '2'}
b = dict.fromkeys([2, 3], [4, 5])
print(a)
print(b)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    print(n, 'is a prime number')

print('---------------------------------')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

a = 1
b = 2
c = 3
print(c)

# c = c * a + b  # c = 5
# print(c)
#
# c *= a + b  # c = 9，其中 a + b 视作一个整体
# print(c)

# c = c * a * b
# print(c)

c *= a * b
print(c)

from functools import reduce
s = "2552551113"
a = [(0,3),(3, 5),(5, 7), (7,10)]

for i, j in a:
    res = s[i:j]
    print(res)
res = '.'.join(s[i:j] for i, j in a)
print(res)


dp = [[4] * 0 for _ in range(0)]
print(dp)

print('-11'.isdigit())

print(eval('-0.5+-3*-4'))

a = iter([1, 2, 3])
# try:
#     print(next(a))
#     print(list(a))  # 使用 list 会改变迭代器本身数据。
#     print(next(a))
#     print(a)
# except StopIteration:
#     print('hha')

print(next(a))
print(list(a))
print(a)  # a 仍然是一个迭代器，但再无法迭代了。
# a = iter(a)
# print(a)  # 还是原来的地址，并没什么差别
# print(next(a))


