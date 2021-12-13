class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = iterator
        self.idx = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums[self.idx]

    def next(self):
        """
        :rtype: int
        """
        num = self.nums[self.idx]
        self.idx += 1
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.nums)


peekingIterator = PeekingIterator([1, 2, 3])  # [1,2,3]
print(peekingIterator.next())    # 返回 1 ，指针移动到下一个元素 [1,2,3]
print(peekingIterator.peek())    # 返回 2 ，指针未发生移动 [1,2,3]
print(peekingIterator.next())    # 返回 2 ，指针移动到下一个元素 [1,2,3]
print(peekingIterator.next())    # 返回 3 ，指针移动到下一个元素 [1,2,3]
print(peekingIterator.hasNext())  # 返回 False
