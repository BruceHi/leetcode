c = ['ddd', 'ccc', 'ssssss']
# a = zip(*c)
# print(list(a))
# for i in zip(*c):
#     print(i)
print(list(zip(*c)))

a = ['a', 'b', 'c']
# b = []
# b = set()
# b = ()
# b = {}
b = ''
print(list(zip(a, b)))

a = 0
b = 1
a, b = b, a+b
print(a, b)

*b, = {'weight': 50, 'name': 'Bob', 'age': 20}
print(b)
*d, = 1, 2, 3
print(type(d))

list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print ('列表插入元素后为 : ', list1)