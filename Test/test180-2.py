def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


str1, str2 = read_file('a.txt'), read_file('b.txt')
str3 = ''.join(sorted(str1+str2))
with open('c.txt', 'w') as f:
    f.write(str3)

import time
from time import strftime, strptime
print(time.time())
print(type(time.time()))

print(time.localtime(time.time()))

print(time.localtime())

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

print(time.asctime(time.localtime()))

print(time.strptime('2021-04-22 10:54:28', '%Y-%m-%d %H:%M:%S'))

from datetime import datetime, date, time
print(datetime.today())
print(type(datetime.today()))

print(date.today())
print(type(date.today()))

print(datetime.time)

# print(type(datetime.today()))

# print(datetime.date())

a = datetime.today()
print(a.strftime('%S'))