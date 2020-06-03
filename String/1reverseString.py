# 使用递归
# def reverseString(s):
#     def helper(left, right):
#         if left < right:
#             s[left], s[right] = s[right], s[left]
#             helper(left + 1, right - 1)
#
#     helper(0, len(s) - 1)


# 双指针
# def reverse_string(s) -> None:
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left, right = left + 1, right - 1

def reverse_string(s) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left+1, right-1


string = ["h","e","l","l","o"]
reverse_string(string)
print(string)

string = ["H","a","n","n","a","h"]
reverse_string(string)
print(string)
