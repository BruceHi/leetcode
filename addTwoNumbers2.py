# 445. 两数相加2
# 与 2.两数相加 比，这里是顺序的，而第二题是逆序的。
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     nums1 = 0
    #     while l1:
    #         nums1 = nums1 * 10 + l1.val
    #         l1 = l1.next
    #
    #     nums2 = 0
    #     while l2:
    #         nums2 = nums2 * 10 + l2.val
    #         l2 = l2.next
    #
    #     num = nums1 + nums2
    #     if num == 0:
    #         return ListNode(0)
    #     cur = dummy = ListNode(0)
    #     nums = []
    #     while num:
    #         nums.append(num % 10)
    #         num //= 10
    #     for num in reversed(nums):
    #         cur.next = ListNode(num)
    #         cur = cur.next
    #     return dummy.next

    # 使用头插法，用了哑节点
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     stack1, stack2 = [], []
    #     while l1:
    #         stack1.append(l1.val)
    #         l1 = l1.next
    #     while l2:
    #         stack2.append(l2.val)
    #         l2 = l2.next
    #     carry = 0
    #     dummy = ListNode(0)
    #     while stack1 or stack2 or carry:
    #         num = (stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0) + carry
    #         carry = num // 10
    #         val = num % 10
    #         new = ListNode(val)
    #         dummy.next, new.next = new, dummy.next
    #     return dummy.next

    # 不需要哑节点，只需要一个指针永远指向第一位即可
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        res = None
        while stack1 or stack2 or carry:
            num = (stack1.pop() if stack1 else 0) + (stack2.pop() if stack2 else 0) + carry
            carry = num // 10
            val = num % 10
            new = ListNode(val)
            new.next = res
            res = new
        return res


def generate_link(nums: List[int]) -> ListNode:
    head = ListNode(0)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next


def print_link(head: ListNode) -> None:
    res, cur = [], head
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


s = Solution()
a = generate_link([7, 2, 4, 3])
b = generate_link([5, 6, 4])
print_link(s.addTwoNumbers(a, b))
