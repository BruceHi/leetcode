from collections.abc import Iterable
print(list(range(10)))
print(range(1, 10))
print(list(range(1, 10)))


# 处理多个银行账户的余额信息
def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)


# def test():
# #     amounts = [1000, 105, 3500, 739]
# #     rate = 0.05
# #     addInterest(amounts, rate)
# #     print(amounts)
# #
# #
# # test()
amounts = [1000, 105, 3500, 739]
rate = 0.05
addInterest(amounts, rate)
print(amounts)

print(range(4, 4))
print(list(range(4, 4)))

if range(4, 4) == False:
    print('a')
for i in range(4, 5):
    print("hello")

L=['Google', 'Runoob', 'Taobao']
print(L[1:])
print(L[1:2])

list1 = [1, 3, 4, 3, 2, 1]

list1 = set(list1)

print(list1)

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)
print(site)

num = 12345
print(int(str(num)))
x = list(map(int,str(num)))
print(x)

num = 125

# print(map(int, num))
print(list(map(int, str(num))))

# a = {1, 2, 3, 2, 3, 6, 5,5 }
# print(a)
# print(a[0])

list1 = ['c', 'a']
print(''.join(list1))

list1 = [1]
print(list1[-1])

#
num_list = [1, 2, 3, 4, 5]
print(num_list)

# for i in range(len(num_list)):
#     if num_list[i] == 2:
#         num_list.pop(i)
#     else:
#         print(num_list[i])
#
# print(num_list)


from collections import Iterator
digits = [9, 9, 9]
digits = map(str, digits)  # 使digits 变成由字符（串）组成的列表
print(digits)

print(isinstance(digits, Iterable))
print(type(digits))
nums = int(''.join(digits)) + 1
print(nums)

print(isinstance((x for x in {1, 5}), Iterator))
print(isinstance((x for x in {1, 5}), Iterable))

print(isinstance({1, 5}, Iterable))
print(isinstance({1, 5}, Iterator))

num_list = [1, 2, 3, 4, 5]
print(num_list)
#
# for i in range(len(num_list) * 1):
#     if num_list[i] == 2:
#         num_list.pop(i)
#     else:
#         print(num_list[i])
#
# print(num_list)

print("-91283472332")


print("abc\r\ncba\rrr\bz\n")
print("abcd\b\b")


print('ecdf\vasss')

print('ec\rdf')
print('ec\ndf\be')
print('ec\vdf')
print('ecdfasss')
print('hello','\v','dd')
print('hello','\f','dd')