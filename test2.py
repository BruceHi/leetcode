num_list = [1, 2, 3, 4, 5]
print(num_list)
#
# for i in range(len(num_list)):
#     if num_list[i] == 2:
#         num_list.pop(i)
#     else:
#         print(num_list[i])

print(num_list)
a = -101
print(a//(-10))

print(-3//-7)

print(list(range(0)))

list1 = list(filter(str.isalnum, "Colour Temperature is 2700 Kelvin"))
print(list1)

s = "A man, a plan, a canal: Panama"
s = list(filter(str.isalnum, s.lower()))
print(str.isalnum('a'))
print(s)

print(int('  -6  '))



print(list(range(-6)))

c = [1,2,3]

print(c[-4:-1])
print(c[0:8])
# import re
#
# key = r'abc'
# p = r'd'
# pattern = re.compile(p)
# matcher = pattern.search(key)
# print(matcher.group())
# print(int())


# c = [1,2,3]
# print(c[7])

# d ='abc'
# print(d[-8])

# c = ('a', 'b')
# print(c[3])

print('-----------method4-----------')
a, b = 'Hello', 'word'
c = a, b
print(a, b)
print(c)
print(type(c))

s = 'adsfg'
for i in s[1:]:
    print(i)
