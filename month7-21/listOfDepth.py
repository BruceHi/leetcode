# 面试题 04.03. 特定深度节点链表
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        queue = deque([tree])
        res = []
        while queue:
            cur = dummy = ListNode(0)
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.next = ListNode(node.val)
                cur = cur.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(dummy.next)
        return res


