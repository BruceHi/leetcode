# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 使用额外空间
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:
#         num = []
#         while head:
#             num.append(head.val)
#             head = head.next
#         i, j = 0, len(num)-1
#         while i < j:
#             if num[i] != num[j]:
#                 return False
#             i, j = i + 1, j - 1
#         return True

# 使用快慢指针，部分反转链表
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next  # 就算为None,slow也要往前走一步,仅针对偶数链表
            slow.next, pre, slow = pre, slow, slow.next

        node1 = pre
        node2 = slow.next if fast else slow  # 奇为slow.next

        while node1:
            if node1.val != node2.val:
                return False
            node1, node2 = node1.next, node2.next
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


x = input_linklist(1, 2, 2, 1)
s = Solution()
print(s.isPalindrome(x))


