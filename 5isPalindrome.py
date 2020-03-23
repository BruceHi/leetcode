# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         copy = ListNode(0)  # 数据结构后面要改变，所以先备份一下。
#         first = copy
#         while head:
#             value = head.val
#             copy.next = ListNode(value)  # 必须要新建对象，否则还是指向原来的链表。
#             head = head.next
#             copy = copy.next

#         second = reverseList(head)  # 调用过该函数head.next就变成了None. 因为是反向链表。
#         # print(output_linklist(new))
#         # print(head.next.val)
#         # print(cur.next.val)
#         first = first.next
#         # print(first.next.next.val)
#         while first:
#             if first.val != second.val:
#                 return False
#             first = first.next
#             second = second.next
#         return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num = []
        while head:
            num.append(head.val)
            head = head.next
        i, j = 0, len(num)-1
        while i < j:
            if num[i] != num[j]:
                return False
            i, j = i + 1, j - 1
        return True


def output_linklist(link):
    while link:
        print(link.val)
        link = link.next


def input_linklist(*val):
    prehead = ListNode(0)
    result = prehead
    for i in val:
        prehead.next = ListNode(i)
        prehead = prehead.next
    return result.next


# x = ListNode(1)
# x.next = ListNode(2)
# x.next.next = ListNode(3)
# x.next.next.next = ListNode(4)

x = input_linklist(1, 2, 2, 1)
s = Solution()
# # y = reverseList(x)
# output_linklist(y)
print(s.isPalindrome(x))


