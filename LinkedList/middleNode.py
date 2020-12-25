# 876. 链表的中间节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


def generate_link(nums):
    cur = dummy = ListNode(0)
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_link(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)


s = Solution()
head = generate_link([1, 2, 3, 4, 5])
print_link(s.middleNode(head))

head = generate_link([1, 2, 3, 4, 5, 6])
print_link(s.middleNode(head))