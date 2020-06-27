# 旋转链表
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # # 转换为列表，旋转一下，再转换回去。
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if not k or not head:
    #         return head
    #     nums, cur = [], head
    #     while cur:
    #         nums.append(cur.val)
    #         cur = cur.next
    #
    #     n = len(nums)
    #     k %= n
    #     nums[:] = nums[::-1]
    #     nums[:] = nums[:k][::-1] + nums[k:][::-1]
    #
    #     cur = dummy = ListNode(0)
    #     for num in nums:
    #         cur.next = ListNode(num)
    #         cur = cur.next
    #     return dummy.next

    # 连成环
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:  # head 为 none，或只有一个结点
            return head

        n, cur = 1, head
        while cur.next:  # 可以定位到最后一个结点
            n += 1
            cur = cur.next
        cur.next = head  # 首尾相连

        cur = head
        for _ in range(n - k % n - 1):  # 定位到前驱结点，即新的尾结点
            cur = cur.next
        new_head = cur.next
        cur.next = None

        return new_head


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
a = generate_link([1, 2, 3, 4, 5])
print_link(s.rotateRight(a, 2))

a = generate_link([0, 1, 2])
print_link(s.rotateRight(a, 4))

a = generate_link([])
print_link(s.rotateRight(a, 0))
