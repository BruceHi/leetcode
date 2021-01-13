a = '11112'
print(a.rindex('1'))

c = [2,3,1,1,4]
print(c.index(1))

for i, a in enumerate(reversed(c)):
    if a == 1:
        print(i)
        break

n = len(c) - 1 - list(reversed(c)).index(1)
print(n)

from collections import Counter

b = Counter('abc') - Counter('ab')
print(Counter('abc') - Counter('ab'))
print((Counter('abc') - Counter('ab')).elements())
print(list(b))
print(list(b.keys()))

c = Counter('aabc')
c['a'] -= 3
print(c)
c.pop('a')
print(c)

a = 123
print()