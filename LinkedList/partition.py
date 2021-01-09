from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre = dummy = ListNode(0)
        dummy.next = head
        pre2 = dummy2 = ListNode(0)

        while pre.next:
            cur = pre.next
            if cur.val < x:
                pre.next = cur.next
                pre2.next = cur
                pre2 = pre2.next
            else:
                pre = pre.next
        pre2.next = dummy.next
        return dummy2.next


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
head = generate_link([1, 4, 3, 2, 5, 2])
print_link(s.partition(head, 3))

head = generate_link([5,1,4,3,2,5,2])
print_link(s.partition(head, 4))
