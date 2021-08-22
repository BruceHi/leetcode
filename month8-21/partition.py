from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 分别取出数据数组，然后拼接
    # def partition(self, head: ListNode, x: int) -> ListNode:
    #     nums1, nums2 = [], []
    #     cur = head
    #     while cur:
    #         if cur.val < x:
    #             nums1.append(cur.val)
    #         else:
    #             nums2.append(cur.val)
    #         cur = cur.next
    #
    #     pre = dummy = ListNode(0)
    #     for num in nums1:
    #         pre.next = ListNode(num)
    #         pre = pre.next
    #
    #     for num in nums2:
    #         pre.next = ListNode(num)
    #         pre = pre.next
    #
    #     return dummy.next

    def partition(self, head: ListNode, x: int) -> ListNode:
        headA, headB = ListNode(0), ListNode(0)
        curA, curB = headA, headB

        while head:
            if head.val < x:
                curA.next = head
                curA = curA.next
            else:
                curB.next = head
                curB = curB.next
            head = head.next

        curA.next = headB.next
        curB.next = None

        return headA.next


def generate_link(nums: List[int]) -> ListNode:
    cur = head = ListNode(0)
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
a = generate_link([1,4,3,2,5,2])
print_link(s.partition(a, 3))

a = generate_link([2, 1])
print_link(s.partition(a, 3))
