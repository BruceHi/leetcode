from collections import deque


print(deque([]))
print(type(deque([])))

print(deque([]) == [])
print(deque([]) == deque())
print(deque([]) == deque([]))

print(deque([]) == deque([1, 2]))

a = 0b10100
# c = -a
print(type(a))
print(a)
print(a & -a)
print(bin(a & -a))

for dx, dy in zip([1, 1, -1, -1], [1, -1, 1, -1]):
    print(dx, dy)


import re
key = r'The car parked in the garage.'
p1 = r'(T|t)he|car'
pattern = re.compile(p1)
print(pattern.findall(key))

key = r'<h1>hello world<h1><h2>hello fuck<h2><h3>hello pc<h3><h4>hello dd<h4><h5>hello god<h5>'
p1 = r'(?<=(<h[1-5]>))(.+?)(?=\1)'  #  再添加一个捕获组，则我们所需内容为 group2。
pattern = re.compile(p1)
s = pattern.findall(key)
print(s)  # 输出未提取的原始内容，对比项。
# print([a for _, a in s])  # 获取 group2。与下面语句等效。
_, b = zip(*s)
print(list(b))

a = '1jj kk5 jj '
print(a.split())
print(a.strip())


a = [1] * 0
print(a)

import random
print(random.randrange(1, 5))

