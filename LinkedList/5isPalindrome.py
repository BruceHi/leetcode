# 判断是否是回文链表
# Definition for singly-linked list.
from typing import List


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

# # 使用快慢指针，部分反转链表
# class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     slow, fast, pre = head, head, None
    #     while fast and fast.next:
    #         fast = fast.next.next  # 就算为None,slow也要往前走一步,仅针对偶数链表
    #         slow.next, pre, slow = pre, slow, slow.next
    #
    #     node1 = pre
    #     node2 = slow.next if fast else slow  # 奇为slow.next
    #
    #     while node1:
    #         if node1.val != node2.val:
    #             return False
    #         node1, node2 = node1.next, node2.next
    #     return True

class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     pre, slow, fast = None, head, head
    #     while fast and fast.next:
    #         fast = fast.next.next  # 必须放在前面，因为后面的语句会改变指向。
    #         slow.next, pre, slow = pre, slow, slow.next
    #
    #     left = pre
    #     right = slow.next if fast else slow
    #
    #     while left:
    #         if left.val != right.val:
    #             return False
    #         left, right = left.next, right.next
    #
    #     return True

    # # 翻转部分链表
    # def isPalindrome(self, head: ListNode) -> bool:
    #     pre, cur = None, head
    #     fast = head
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         cur.next, pre, cur = pre, cur, cur.next
    #
    #     if fast:  # 奇数链表
    #         cur = cur.next
    #     while pre:
    #         if pre.val != cur.val:
    #             return False
    #         pre, cur = pre.next, cur.next
    #     return True

    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]


def generate_link(nums: List[int]) -> ListNode:
    head = ListNode(0)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next


s = Solution()
x = generate_link([1, 2, 2, 1])
print(s.isPalindrome(x))

x = generate_link([1, 2, 3, 2, 1])
print(s.isPalindrome(x))

x = generate_link([1, 2, 3, 2, 4])
print(s.isPalindrome(x))