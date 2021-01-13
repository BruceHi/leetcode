board = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]
m, n = len(board), len(board[0])
board_copy = [[0] * (n+2)] + [[0] + row[:] + [0] for row in board] + [[0] * (n+2)]
print(board_copy)

from copy import copy
from collections import deque

a = deque([1, 23, 4, [1, 2]])
b = copy(a)

a.append(9)
print(b)

a[-2][0] = 3
print(b)

# queue = deque([1, 2, 4, 5])
# for i in queue[:1]:
#     print(i)
# print(queue[3:4])

c = [1, 2, 3]
print(c.index(2))

n = 0b0000010100101000001111010011100
print(bin(n))
print(type(bin(n)))
# print(str(0b100))

print(n)
a = n
print(bin(a))

print(int(a))

print(str(a))  # 不能直接 str，这就相当于转换为 10 进制，然后 str。
print(str(bin(a)))

# print(''.join(reversed(str(bin(a))))[:-2])
#
# c = ''.join(reversed(str(bin(a))))[:-2]
# print(bin(int(c)))

# print('0b10')
# print(int('10111', base=2))
# # print(int('10300', base=2))  #  转换为 2 进制
# print(int('0b10111', base=0))
# print(int('d10'))

print('31' > '3')
print(all([1, 1, 1]))

print(all([1, 1, 0]))

print(any([1, 1, 0]))

print(any([0, 0, 0]))

a = [1, 2, 3]
print(a.count(4))

print(1e9+7)
print(1e9)
a = 10.24e2
print(a)

from collections import Counter
print(Counter('123'))
# print(Counter('123') in Counter('1234'))

print(Counter('123') - Counter('124'))

print(Counter('124') - Counter('123'))

print(Counter('1234') - Counter('124'))

print(Counter('123') - Counter('1234'))

print(Counter('123') - Counter('1234') is None)

print((Counter('123') - Counter('1234')) is True)

print((Counter('123') - Counter('1234')) is False)

print(type(Counter()))

print((Counter('123') - Counter('1234')) == Counter())

print()

print(Counter() is True)
print(Counter() is False)

if Counter() is None:
    print('hello')

if Counter('111'):
    print('hloo')

print([] is True)
print([] is False)
