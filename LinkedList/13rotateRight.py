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
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if not head or not head.next:  # head 为 none，或只有一个结点
    #         return head
    #
    #     n, cur = 1, head
    #     while cur.next:  # 可以定位到最后一个结点
    #         n += 1
    #         cur = cur.next
    #     cur.next = head  # 首尾相连
    #
    #     cur = head
    #     for _ in range(n - k % n - 1):  # 定位到前驱结点，即新的尾结点
    #         cur = cur.next
    #     new_head = cur.next
    #     cur.next = None
    #
    #     return new_head

    # 推荐使用连成环
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if not head or not head.next:
    #         return head
    #
    #     n = 1
    #     cur = head
    #     while cur.next:
    #         n += 1
    #         cur = cur.next
    #     cur.next = head
    #
    #     cur = head
    #     for _ in range(n - k % n - 1):
    #         cur = cur.next
    #     new = cur.next
    #     cur.next = None
    #
    #     return new

    # 找到断开的位置
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if not k:
    #         return head
    #     if not head:
    #         return
    #     dummy = ListNode(0)
    #     dummy.next = head
    #
    #     end = cur = head
    #     n = 0
    #     while cur:
    #         n += 1
    #         end = cur
    #         cur = cur.next
    #
    #     k %= n
    #     if k == 0:
    #         return head
    #     slow = fast = dummy
    #     for _ in range(k+1):
    #         fast = fast.next
    #
    #     while fast:
    #         slow, fast = slow.next, fast.next
    #     dummy.next, end.next = slow.next, dummy.next
    #     slow.next = None
    #     return dummy.next

    # # 转换为列表，旋转一下，再转换回去。
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if not k or not head:
    #         return head
    #     nodes, cur = [], head
    #     while cur:
    #         nodes.append(cur)
    #         cur = cur.next
    #
    #     n = len(nodes)
    #     k %= n
    #     nodes[:] = nodes[::-1]
    #     nodes[:] = nodes[:k][::-1] + nodes[k:][::-1]
    #
    #     cur = dummy = ListNode(0)
    #     for node in nodes:
    #         cur.next = node
    #         cur = cur.next
    #     cur.next = None
    #     return dummy.next

    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if k == 0 or not head or not head.next:
    #         return head
    #
    #     cur = head
    #     n = 1
    #     while cur.next:
    #         n += 1
    #         cur = cur.next
    #     cur.next = head
    #
    #     # 定位到前驱节点，跟上面代码不同的是没有 cur = head这一步，下面循环步数也不用减一
    #     for _ in range(n - k % n):
    #         cur = cur.next
    #     new = cur.next
    #     cur.next = None
    #     return new

    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if not head or not k:
    #         return head
    #     cur = head
    #     n = 0
    #     while cur:
    #         end = cur
    #         cur = cur.next
    #         n += 1
    #
    #     k = k % n
    #     if k == 0:
    #         return head
    #     cur = pre = dummy = ListNode(0)
    #     dummy.next = head
    #     for _ in range(k + 1):
    #         cur = cur.next
    #     while cur:
    #         pre, cur = pre.next, cur.next
    #     dummy.next, end.next = pre.next, dummy.next
    #     pre.next = None
    #     return dummy.next

    # 成环
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not k or not head or not head.next:
            return head
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head

        for _ in range(n-k%n):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head




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

a = generate_link([1])
print_link(s.rotateRight(a, 0))

a = generate_link([])
print_link(s.rotateRight(a, 1))

a = generate_link([1])
print_link(s.rotateRight(a, 1))

a = generate_link([1, 2])
print_link(s.rotateRight(a, 2))
