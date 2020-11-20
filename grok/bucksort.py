# 桶排序，非原地算法，时间复杂度为 O(n+k)，空间复杂度为 O(n+k)。

# def buck_sort(nums):
#     n = len(nums)
#     min_n = min(nums)
#     max_n = max(nums)
#
#     # 区间范围
#     buck_range = (max_n - min_n) / n
#
#     # 1.分桶。桶数量：len(nums) + 1，最后一个桶实际上是 [max, max]
#     buck_list = [[] for _ in range(n+1)]
#
#     # 2.入桶 TypeError: list indices must be integers or slices, not float
#     # 因为 buck_range 是浮点数，所以使用了 // 也是浮点数。会显示 比如 2.0 之类的整数后面带.0 的形式。
#     # 所以要使用 int
#     for num in nums:
#         buck_list[int((num-min_n)//buck_range)].append(num)
#         # buck_list[int((num - min_n) / buck_range)].append(num)
#
#     # 3.内部排序
#     for i in range(n):
#         buck_list[i].sort()
#
#     # 4.输出
#     res = []
#     for i in range(n+1):  # 桶个数是 n + 1
#         for j in range(len(buck_list[i])):
#             res.append(buck_list[i][j])
#     return res


def buck_sort(nums):
    n = len(nums)
    max_n, min_n = max(nums), min(nums)

    buck_range = (max_n - min_n) / n
    buck_list = [[] for _ in range(n+1)]

    for num in nums:
        buck_list[int((num-min_n)//buck_range)].append(num)

    # 内部排序和输出写一块了
    res = []
    for buck in buck_list:
        buck.sort()
        res.extend(buck)
    return res


x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(buck_sort(x))

nums = [1, 4, 5, 6, 5, 6]
print(buck_sort(nums))


nums = [1, 2, 3, 4, 5]
print(buck_sort(nums))
