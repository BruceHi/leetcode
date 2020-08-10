s = "3[a]2[bc]"
for char in s:
    print(type(char))

from collections import deque
s = deque()
s.append('d')
print(s)
print(list(s))

print('b'.isalpha())
print('3'.isnumeric())

n = 3
n *= 3 + 4
print(n)

import re
s = re.split(r'\W+', 'runoob, runoob, runoob.')
print(s)

# 首尾处若有 \W 捕获到的，则分割的时候会有空字符‘’
# 如果在模式中使用了捕获括号，则模式中所有组的文本也将作为结果列表的一部分返回。


s = re.split(r'(\W+)', 'runoob, runoob, runoob.')
print(s)

s = re.split(r'(\W+)', 'runoob, runoob, runoob.')
print(s)

s = re.split('\W', ' runoob, runoob, runoob.', 1)
print(s)

# ValueError: split() requires a non-empty pattern match.
# 所以不要使用 *， 用 + 来替代
# s = re.split(r'd*', 'hello, world')
# c = re.compile('dd')


print(s)

from collections import deque
s = 'ddd'
queue = deque(s[0])
print(queue)

a = [{1:2}, {'d':2}]
print(a[0][1])

# 改正与进入是两回事，改正不影响顺序
from collections import OrderedDict
b = OrderedDict()
b[1] = 2
b[-1] = 3
print(b)
b[1] = 4
print(b)

print('abc' == 'bac')
print(sorted('abc') == sorted('bac'))

print({1:2, 3:4} == {3:4, 1:2})
from collections import Counter

a = '12'
print('dd')


b = Counter(a)
print(b)
print(dict(b))
print({'1':1, '2':1} == b)

p = "abc"
s = dict((i, p.count(i)) for i in p)
print(s)

print(type(str(123)))

print(-123 // 10)

print(-123 % 10)

a = []
print(int(-85))
print(int(*a))


print(int(8.2))
print(int(0xf))
print(int(0b100))

a = [(1, 2), (3, 4)]
# print(a.pop())

# res = []
# res = res + (1, 2, 4)
# print(res)
#
# res.extend((1, 2, 4))
# print(res)

d = (2, 2)
c = set(d)
print(c)

s = {'1': 2}
w = ''
w += str(*s)
print(w)

import bisect

L = [1,3,3,6,8,12,15]
x = 3

print(bisect.bisect_left(L, x))

queue = [3, 4, 5]
for _ in range(len(queue)):
    queue.append(1)
print(queue)

a = '1,2,3,None,3,None,1,'
b = list(a)
print(b)

c = a.split()
# c.pop()
# c[0] = c[0][1]
# c[-1] = c[-1][1]
# d = list(map(int, c))
print(c)
print(id(None))
a = [3, 4, 4, 4, 5]
for i in a:
    print(i, end='\t')

print(id(None))

s = 'leetcode'
t = 'code'
print(s.find(t))
s = s.replace(t, '')
print(s)

a = {4, 2, 6}
# a.add(1)
# a.add(3)
print(a)

print((1, 2) == (2, 1))

row = [set()] * 2
row[0].add(1)
print(row)

row = [set() for _ in range(2)]
row[0].add(1)
print(row)

from collections import defaultdict
from collections import Counter
# count = Counter()
count = defaultdict(int)
count['a'] = 3
count['b'] = 4
count['c'] += 2
print(count)

a = 2
a += 4 + 4
print(a)

print([1, None, 2])

a = [[0] * 3] * 3
print(a)

a[0][0] = 1
print(a)

print([1, 2, 3] == [3, 2, 1])

# b = input()dd
# print(type(b))
# s, t = [input()] * 2
# print(s, t)



