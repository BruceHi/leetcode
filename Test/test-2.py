a, b = '1', '90'
print(eval(a + b))

c = '1+56*2'
print(eval(c))
print(type(eval(c)))

a = {'a': 2, 'b': 1, 'c': 0}
d = 'aab'
from collections import Counter
dic = Counter(d)
print(dic)
print(a == dic)

a = [1, 2, 3, 4]
print(map(lambda x: -x, a))
print(list(map(lambda x: -x, a)))
print([*map(lambda x: -x, a)])
# list 与 [*] 的作用相同。

from collections import defaultdict
a = defaultdict(bool)
print(a[1])
print(a[2])

s = '1,2,,,3,4,,,5,,'
print(s.split(','))

s = '1,2,None,None,3,4,None,None,5,None,None,'
print(s.split(','))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*matrix)))

print(list(map(list, zip(*matrix))))

print(list(map(list, zip(*matrix)))[::-1])

print(list(zip(*matrix))[::-1])

a = '123'

print(type(a[1:]))

a = []
print(a[0:0])

# a[:] = 1, 2

a[0:3] = [2]
print(a)

# 赋值要可迭代对象
a[0:0] = [3]

a[2:2] = [4]
print(a)
a.insert(10, [45])
print(a)

a = list(range(1, 11))
print(a)

res = []
for num in a[:-1]:
    res.append([num, num+0.9])
print(res)

res = [[1, 1.9]]
for _ in range(9):
    res.append([res[-1][-1], res[-1][-1]+0.9])
print(res)

print((2-1) // 0.8)
print(int((2-1)/0.8))

# // 是地板除，
print(6/2)
print(6//2.7)
