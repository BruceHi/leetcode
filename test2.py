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
