# 138.复制带随机指针的链表
from typing import List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # 创建一个哈希表，key是原节点，value是新节点
    # 第一次遍历，将原节点和新节点放入哈希表中，顺便把 next 给连好
    # 第二次遍历，将 random 连好
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        p = head
        cur = dummy = Node(0)
        while p:
            new = Node(p.val)
            dic[p] = new
            cur.next = new
            cur = cur.next
            p = p.next

        while head:
            if head.random:
                dic[head].random = dic[head.random]
            head = head.next
        return dummy.next


def generate_Nodes(nums) -> Node:
    head = Node(0)
    cur = head
    record = []  # 记录节点相对顺序
    for num, _ in nums:
        new = Node(num)
        record.append(new)
        cur.next = new
        cur = cur.next

    p = head.next
    for _, rand in nums:
        if rand is not None:
            p.random = record[rand]
        p = p.next
    return head.next


def print_Nodes(head: Node) -> None:
    record = []
    cur = head
    while cur:
        record.append(cur)
        cur = cur.next

    res, cur = [], head
    while cur:
        if cur.random is None:
            res.append([cur.val, None])
        else:
            res.append([cur.val, record.index(cur.random)])
        cur = cur.next
    print(res)


# head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
# a = generate_Nodes(head)
# print_Nodes(a)
s = Solution()
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
head = generate_Nodes(head)
print_Nodes(s.copyRandomList(head))

head = [[1,1],[2,1]]
head = generate_Nodes(head)
print_Nodes(s.copyRandomList(head))

head = [[3, None],[3,0],[3, None]]
head = generate_Nodes(head)
print_Nodes(s.copyRandomList(head))

head = []
head = generate_Nodes(head)
print_Nodes(s.copyRandomList(head))
