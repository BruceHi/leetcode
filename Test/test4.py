print([0]*10)

string = '('
print(ord(string))

string = ')'
print(ord(string))

if ord('(') + 1 == ord(')'):
    print('yes')

if ord('[') + 2 == ord(']'):
    print('yes')

if ord('{') + 2 == ord('}'):
    print('yes')

if '[' + '2' == ']':
    print('no')

print([0] * 5)

import operator
s = '+'
if s == '+':
    operator.add(4, 5)

i = '2'
print(i.isdigit())

a = 4
b = 3.5
print(operator.ifloordiv(a, b))
print(operator.floordiv(a, b))
print(operator.itruediv(a, b))
print(int(-0.2))
print(int(-5.2))

print([1] + [2])
print('[' + '2')
# a = []
# a.append([])
# print(a)
# a[0].append(3)

a = [1, 4, 5]
print(set(a))

print(sorted(a))
print(len(a))

e, f = 3, 4

print(e > f)

b = [1, 1]
print(sorted(set(b)))
print(b == list(sorted(set(b))))

weather = ['good', 'not good', 'well', 'very well']
for i, v in enumerate(weather, 1):
    print(i, v)

# s = 'hello'
# s[:2] = 'hh'
# print(s)

# s = (1, 2, 3)
# s[:2] = (1, 3)

# a = [1, 4, 3]
# a[1:2] = 30
# print(a)

a = [1, 2, 3, 4]
a[1:3] = (30,)
print(a)

a = [1, 2, 3, 4]
a[1:3] = [30]
print(a)

# site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# pop_obj = site.pop(default='d')
# print(pop_obj)
# print(site)

print(type(int('-7')))
if None:
    print('haeel')

a = [1, 2]
a.append('')
print(a)

from copy import deepcopy
b = [1, 2, 3, 1]
c = deepcopy(b)
b.reverse()
print(b)
print(c)

dp = [[0] * 2] * 2
print(dp)

dp = [[[0, 0]] * 3] * 8
for k in range(3):
    dp[0][k][1] = float('-inf')
    dp[-1][k][1] = float('-inf')
print(dp)

dp = [[[0 for i in range(2)] for i in range(3)] for i in range(8)]
for k in range(3):
    dp[0][k][1] = float('-inf')
    dp[-1][k][1] = float('-inf')
print(dp)

dp = [[0, 0] for _ in range(2)]  # 表示内部元素乘与 n,与 [0]*n 是一个效果， dp 存的都是可获得利益最大值
dp[-1][0], dp[-1][1] = 0, float('-inf')
print(dp)

dp = [[0 for _ in range(2)] for _ in range(2)]  # 表示内部元素乘与 n,与 [0]*n 是一个效果， dp 存的都是可获得利益最大值
dp[-1][0], dp[-1][1] = 0, float('-inf')
print(dp)

dp_i0, dp_i1 = [0]*2, [float('-inf')]*2
print(dp_i0)
print(dp_i1)