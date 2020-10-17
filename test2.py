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

