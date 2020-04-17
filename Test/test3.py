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

nums = [1, 0, 0, 3, 0, 5]

# 正序遍历
# 正序正数索引
# for i in range(len(nums)):
#     temp = i
#     if not nums[i]:
#         nums.pop(i)
#
# print(nums)

for i in nums:
    temp = i
    if not i:
        nums.remove(i)

print(nums)

# 倒叙正数索引
for i in range(len(nums)-1, -1, -1):
    if not nums[i]:
        nums.pop(i)
#
# print(nums)

# 倒叙负数索引
# for i in range(-1, -len(nums)-1, -1):
#     if not nums[i]:
#         nums.pop(i)
#
# print(nums)

# 正序负数索引
for i in range(-len(nums), 0):
    if not nums[i]:
        nums.pop(i)

print(nums)

i = 0
while i < len(nums) - 1:
    if not nums[i]:
        nums.pop(i)
        i -= 1
    i += 1
print(nums)

print({('d', 'e')})
