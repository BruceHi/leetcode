import datetime
print(datetime.datetime.now())

from collections import Counter
sentence = "I can because i think i can"
# Counter是一个简单的计数器，可以数组中统计字符出现的个数：
counts = Counter(sentence.split())
print(counts)

# import os
# os.remove('demo.txt')



def div_zero(num):
    try:
        a = 10 / num
        print(a)
    except:
        print('num is 0')


div_zero(2)


def judge_num(num):
    if num >= 5:
        raise ValueError('数量不能大于5')
    else:
        return 100


div_zero(2)

judge_num(4)

s = 'hello world'
print(s.upper())
print(s.title())

s = '1222'
a = '222s'
print(s.isdigit())
print(a.isdigit())
s.isdecimal()
print(''.join(reversed(s)))

s = ' adabdw '
print(s.strip())

import chardet

s = 'abd'.encode('gbk')
print(chardet.detect(s))
a = s.decode('gbk').encode('utf-8')
print(chardet.detect(a))

s="info：xiaoZhang 33 shandong"
import re
a = re.split(r'\W', s)
print(a)

s="你好 中国 "
import re
a = re.split(r' ', s)
print(a)

a = [1, 2, 3]
b = [2, 3, 4]
c = set(a) & set(b)
print(c)

print((set(a) - c) | set(b) - c)

a = [[1,2],[3,4],[5,6]]
print(sum(a, []))

print([x for y in a for x in y])

import random
random.shuffle(a)
print(a)

b = {1:2}
# del b['8']
# print(b)

d1 = [
    {'name': 'alice', 'age': 38},
    {'name': 'bob', 'age': 18},
    {'name': 'ctrl', 'age': 28}
]
d1.sort(key=lambda x: x['age'])
print(d1)


a = {"A":1,"B":2}
b = {"C":3,"D":4}

c = dict(**a, **b)
print(c)

a = [(1, 2), (3, 4)]
print({key: val for key, val in a})

a = ("a","b")
b = (1,2)
c = {key: val for key, val in zip(a, b)}
print(c)

print(dict(zip(a, b)))

c = {"A": 1,"B": 2}
print(dict(**c))

a = (x for x in range(100))
print(type(a))
print(a)

import itertools

print(list(itertools.islice(a, 10, 20)))

a="hello"
b="你好"
c = b.encode()
print(b)


a = b"hello"
b = bytes("你好", "utf-8")
c = "你好".encode("utf-8")
print(a, b, c)

import json

dict_demo = {"name": "旭东"}
print(json.dumps(dict_demo, ensure_ascii=False))