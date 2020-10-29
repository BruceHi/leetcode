# 单链表
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class MyLinkedList:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.size = 0
#         self.head = ListNode(0)
#
#     def get(self, index: int) -> int:
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         if index < 0 or index >= self.size:
#             return -1
#         pred = self.head
#         for _ in range(index + 1):
#             pred = pred.next
#
#         return pred.val
#
#     def addAtHead(self, val: int) -> None:
#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#         """
#         self.addAtIndex(0, val)
#
#     def addAtTail(self, val: int) -> None:
#         """
#         Append a node of value val to the last element of the linked list.
#         """
#         self.addAtIndex(self.size, val)
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         """
#         Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
#         """
#         if index > self.size:
#             return
#         if index < 0:
#             index = 0
#         self.size += 1
#
#         pred = self.head
#         for _ in range(index):
#             pred = pred.next
#         add_note = ListNode(val)
#         add_note.next = pred.next
#         pred.next = add_note
#
#     def deleteAtIndex(self, index: int) -> None:
#         """
#         Delete the index-th node in the linked list, if the index is valid.
#         """
#         if index < 0 or index >= self.size:
#             return
#         pred = self.head
#         self.size -= 1
#         for _ in range(index):
#             pred = pred.next
#         pred.next = pred.next.next


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class MyLinkedList:
#
#     def __init__(self):
#         self.size = 0
#         self.head = ListNode(0)
#
#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1
#         curr = self.head
#         for _ in range(index+1):
#             curr = curr.next
#         return curr.val
#
#     def addAtHead(self, val: int) -> None:
#         self.addAtIndex(0, val)
#
#     def addAtTail(self, val: int) -> None:
#         self.addAtIndex(self.size, val)
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.size:
#             return
#         if index < 0:
#             index = 0
#
#         prev = self.head
#         for _ in range(index):  # 找到前驱结点
#             prev = prev.next
#         new = ListNode(val)
#         new.next = prev.next
#         prev.next = new
#         self.size += 1
#
#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return
#         self.size -= 1
#         prev = self.head
#         for _ in range(index):
#             prev = prev.next
#         prev.next = prev.next.next
#
#
#
#
# # Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# # 双链表
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.prev, self.next = None, None
#
#
# class MyLinkedList:
#     def __init__(self):
#         self.size = 0
#         # 定义相连的两个伪节点。
#         self.head, self.tail = ListNode(0), ListNode(0)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1
#         # 选择从头遍历还是尾部遍历
#         if index + 1 <= self.size - index:
#             curr = self.head
#             for _ in range(index+1):  # 定位到该节点
#                 curr = curr.next
#         else:
#             curr = self.tail
#             for _ in range(self.size-index):  # 定位到该节点
#                 curr = curr.prev
#
#         return curr.val
#
#     def addAtHead(self, val: int) -> None:
#         # self.addAtIndex(0, val)
#         self.size += 1
#         add_node = ListNode(val)
#         pred = self.head
#         succ = self.head.next
#         add_node.prev, add_node.next = pred, succ
#         pred.next, succ.prev = add_node, add_node
#
#     def addAtTail(self, val :int) -> None:
#         self.addAtIndex(self.size, val)
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.size:
#             return
#         if index < 0:
#             index = 0
#
#         # 选择：从前遍历到前驱节点，从后遍历到当前节点(后继节点)
#         if index <= self.size - index:
#             pred = self.head
#             for _ in range(index):
#                 pred = pred.next
#             succ = pred.next  # 使用pred，succ表示找到的前驱节点和后继节点
#         else:
#             succ = self.tail
#             for _ in range(self.size-index):
#                 succ = succ.prev
#             pred = succ.prev
#
#         self.size += 1
#         add_note = ListNode(val)
#         add_note.prev, add_note.next = pred, succ
#         pred.next, succ.prev = add_note, add_note
#
#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return
#         # 找到index的前驱和后继节点，选择
#         if index <= self.size-index-1:
#             pred = self.head
#             for _ in range(index):
#                 pred = pred.next
#             succ = pred.next.next
#         else:
#             succ = self.tail
#             for _ in range(self.size-index-1):
#                 succ = succ.prev
#             pred = succ.prev.prev
#
#         self.size -= 1
#         pred.next = succ
#         succ.prev = pred
#
#
# linkedList = MyLinkedList()
# linkedList.addAtHead(1)
# linkedList.addAtTail(3)
# linkedList.addAtIndex(1, 2)   # //链表变为1-> 2-> 3
# print(linkedList.get(1))     # //返回2
# linkedList.deleteAtIndex(1)  # //现在链表是1-> 3
# print(linkedList.get(1))            # 返回3

# 双链表
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.prev, self.next = None, None
#
#
# class MyLinkedList:
#
#     def __init__(self):
#         self.size = 0
#         self.head, self.tail = ListNode(0), ListNode(0)
#         self.head.next, self.tail.prev = self.tail, self.head
#
#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1
#
#         if index + 1 < self.size - index:
#             cur = self.head
#             for _ in range(index+1):
#                 cur = cur.next
#         else:
#             cur = self.tail
#             for _ in range(self.size - index):
#                 cur = cur.prev
#
#         return cur.val
#
#     def addAtHead(self, val: int) -> None:
#         return self.addAtIndex(0, val)
#
#     def addAtTail(self, val: int) -> None:
#         return self.addAtIndex(self.size, val)
#
#     def addAtIndex(self, index: int, val: int) -> None:
#         if index > self.size:
#             return
#         if index < 0:
#             index = 0
#
#         if index < self.size - index:
#             pre = self.head
#             for _ in range(index):
#                 pre = pre.next
#             suc = pre.next
#         else:
#             suc = self.tail
#             for _ in range(self.size-index):
#                 suc = suc.prev
#             pre = suc.prev
#
#         self.size += 1
#         new = ListNode(val)
#         new.prev, new.next = pre, suc
#         pre.next, suc.prev = new, new
#
#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return
#
#         if index < self.size - index - 1:
#             pre = self.head
#             for _ in range(index):
#                 pre = pre.next
#             suc = pre.next.next
#         else:
#             suc = self.tail
#             for _ in range(self.size-index-1):
#                 suc = suc.prev
#             pre = suc.prev.prev
#
#         self.size -= 1
#         pre.next, suc.prev = suc, pre

class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev, self.next = None, None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head, self.tail = ListNode(0), ListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        if index+1 < self.size-index:
            cur = self.head
            for _ in range(index+1):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.size-index):
                cur = cur.prev

        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index < 0:
            index = 0

        if index < self.size - index:
            pre = self.head
            for _ in range(index):
                pre = pre.next
            suc = pre.next
        else:
            suc = self.tail
            for _ in range(self.size-index):
                suc = suc.prev
            pre = suc.prev

        self.size += 1
        new = ListNode(val)
        new.prev, new.next = pre, suc
        pre.next, suc.prev = new, new

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        if index < self.size-index-1:
            pre = self.head
            for _ in range(index):
                pre = pre.next
            suc = pre.next.next
        else:
            suc = self.tail
            for _ in range(self.size-index-1):
                suc = suc.prev
            pre = suc.prev.prev

        self.size -= 1
        pre.next, suc.prev = suc, pre


linkedList = MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)   # //链表变为1-> 2-> 3
print(linkedList.get(1))     # //返回2
linkedList.deleteAtIndex(1)  # //现在链表是1-> 3
print(linkedList.get(1))
