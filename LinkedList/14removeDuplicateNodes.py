# 移除重复结点
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 错误版本
    # def removeDuplicateNodes(self, head: ListNode) -> ListNode:
    #     record, cur = set(), head  # set 会按由大到小自动排序，所以不能使用
    #     while cur:
    #         record.add(cur.val)
    #         cur = cur.next
    #
    #     cur = dummy = ListNode(0)
    #     for num in record:
    #         cur.next = ListNode(num)
    #         cur = cur.next
    #     return dummy.next

    # # 遍历结束后，再重新构造链表
    # def removeDuplicateNodes(self, head: ListNode) -> ListNode:
    #     record, cur = [], head
    #     while cur:
    #         if cur.val not in record:
    #             record.append(cur.val)
    #         cur = cur.next
    #
    #     cur = dummy = ListNode(0)
    #     for num in record:
    #         cur.next = ListNode(num)
    #         cur = cur.next
    #     return dummy.next

    # 构建哈希表，在原有链表上操作
    # def removeDuplicateNodes(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return head
    #     record, pre = {head.val}, head
    #     while pre.next:  # 遍历前驱结点
    #         cur = pre.next
    #         if cur.val not in record:
    #             record.add(cur.val)
    #             pre = pre.next
    #         else:
    #             pre.next = cur.next
    #     return head

    # def removeDuplicateNodes(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return
    #     pre = dummy = ListNode(0)
    #     record = set()
    #     dummy.next = head
    #     while pre.next:
    #         cur = pre.next
    #         if cur.val in record:
    #             pre.next = cur.next
    #         else:
    #             record.add(cur.val)
    #             pre = cur
    #     return dummy.next

    # def removeDuplicateNodes(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return
    #     record, pre = {head.val}, head
    #     while pre.next:
    #         cur = pre.next
    #         if cur.val in record:
    #             pre.next = cur.next
    #         else:
    #             pre = cur
    #             record.add(cur.val)
    #     return head

    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        record = set()
        pre = dummy = ListNode(0)
        dummy.next = head

        while pre.next:
            cur = pre.next
            if cur.val not in record:
                record.add(cur.val)
                pre = pre.next
            else:
                pre.next = cur.next
        return dummy.next

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
a = generate_link([1, 2, 3, 3, 2, 1])
print_link(s.removeDuplicateNodes(a))

a = generate_link([1, 1, 1, 1, 2])
print_link(s.removeDuplicateNodes(a))

a = generate_link([])
print_link(s.removeDuplicateNodes(a))
