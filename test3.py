import bisect

a = []
index = bisect.bisect_right(a, 1)  # 当 a 式空元素时，bisect_left 和 bisect_right 都返回 0
print(index)

a = [3, 4, 5]
index = bisect.bisect_left(a, 3.5)
print(index)

index = bisect.bisect_right(a, 4)
print(index)

index = bisect.bisect(a, 4)
print(index)

print('ha')
b = {4: [1]}
print(b[4][0])

nums = [1, 2, 4]
mid = 5
start = 0
cnt = 0
for i in range(len(nums)):
    while nums[i] - nums[start] > mid:
        start += 1
    cnt += i - start

print(cnt)

print(ord('('))
print(ord(')'))

print(ord('['))
print(ord(']'))

print(ord('{'))
print(ord('}'))
