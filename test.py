
a = [1]
print(a.index(1))
b = '1231'


print(''.join(reversed(b)).index('1'))

import bisect

a = [1, 4, 7]
print(bisect.bisect_right(a, 8))

print({'a':4, 'b':1} == {'b':1, 'a':4})

print()

a = {'a':4, 'b':1}
# a['d'] += 1
# print(a)

from collections import Counter
b = Counter(a)
print(b)

b['d'] += 1
print(b)
b['e'] += 0.3
print(b['e'])

print(1 ^ 0)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print([map(list, zip(*matrix))])

a = [[3],[9,20],[15,7]]
print(a)

print([x[::-1] for i, x in enumerate(a) if i & 1])

print(a[::1])

# a = []
# a.pop()
# print(a)

print(-4 // -3)

print(-4 // 3)
print('-12'.isdecimal())

print(3*2)
print(1 << 3)
print(3 << 1)
print(3 >> 1)

print((9+9)%10)

a = [0] * 4
print(a)

a = [[0] for _ in range(4)]
print(a)

print(0 ^ 1)
print(1 ^ 1)
print(2 ^ 1)
print(3 ^ 1)
print(4 ^ 1)
print(5 ^ 1)


def f1(func):
    def f2(*args, **kwargs):
        # 装饰器实现的功能
        return func(*args, **kwargs)
    return f2


class Fn:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 装饰器实现的功能
        return self.func(*args, **kwargs)


def robust(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except:
            print('Error execute: %s' % actual_do.__name__)
            #traceback.print_exc()
    return add_robust

@robust
def simple():
    return 5 / 0

simple()


def h1(func):
    def h2(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            print('产生异常')
    return h2

@h1
def test():
    list=[]
    return list[100]
test()

print(ord('b')-ord('a'))

nums = [1, 2, 3, 4]
nums[1:3] = [4, 5]
print(nums)

print(len("米好"))