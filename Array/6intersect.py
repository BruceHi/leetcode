# 列表方法，统计一个，删除一个数据
# def intersect(nums1, nums2):
#
#     aide_list = []
#
#     # 使nums1始终都是短的列表
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1
#
#     # 从nums1中取出一个数，放到nums2中遍历，若出现相同的，立马记录该数值，然后删除nums2中数值。然后结束内层循环。
#     # 防止nums1后面再出现一样的数值，不删除就不好办了。
#     for i in range(len(nums1)):
#         for j in range(len(nums2)):
#             if nums2[j] == nums1[i]:
#                 aide_list.append(nums1[i])
#                 nums2.pop(j)
#                 break
#
#     return aide_list


# hash表
def intersect(nums1, nums2):

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m = {}
    for i in range(len(nums1)):
        m[nums1[i]] = m.get(nums1[i], 0) + 1

    k = 0
    for i in nums2:
        if i in m and m[i] > 0:
            nums1[k] = i    # 重复利用了nums1，不用另建空间
            k += 1
            m[i] -= 1

    return nums1[:k]


list1 = [1,2,2,1]
list2 = [2,2]
print(intersect(list1, list2))

list1 = [4,9,5]
list2 = [9,4,9,8,4]
print(intersect(list1, list2))