import heapq
from itertools import product, permutations, combinations, combinations_with_replacement

a = [4, 8, 3, 7, 3, 6, 3, 4]
heapq.heapify(a)
print(a)

print(list(product('ABCD', 'xy')))

# print(list(product('AD', 'xy','12', repeat=2)))
# print(len(list(product('AD', 'xxy', repeat=2))))

def product2(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

print(list(product2('abc', 'xy')))

a = list(product(range(2), repeat=2))
print(list(product(range(2), repeat=2)))

print(type(a[0][0]))

a = list(product('ab', range(2), 'd'))
print(a)

a = list(permutations('ABCD', 2))
print(a)

a = list(permutations([1, 2, 1]))
print(a)

a = list(permutations([1, 2, 'c']))
print(a)

a = list(combinations([1, 2, 3], 2))
print(a)
a = list(combinations_with_replacement([1, 2, 3], 2))
print(a)


a = [1, 2, 3]
print(2 * a)

# print(-a)
#
# a = {1, 2}
# b = a.__new__()
# print(b)

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(matrix[2])
for i in range(len(matrix)):
    print(matrix[i][2])

res = [matrix[i][2] for i in range(len(matrix))]
print(res)

a = []
b = [num for num in a].append('e')
d = [num for num in a]
print(b)
print(d)

e = []
c = e.append('s')
print(e)

print([1, 2, 1].count(1))



a = [1, 2, 3]
b = [2, 3, 4, 5]
c = [6, 7, 7, 9, 10]

print(list(zip(a, b, c)))

from math import sqrt

print(sqrt(5))

def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)


res = [''] * 5
print(res)