# 实现字典树
# class Trie:
#
#     def __init__(self):
#         self.root = {}
#
#     def insert(self, word: str) -> None:
#         node = self.root
#         for char in word:
#             node = node.setdefault(char, {})  # 遍历结束时，node 指向的是 {}
#         node['#'] = '#'
#
#     def search(self, word: str) -> bool:
#         node = self.root
#         for char in word:
#             if char not in node:
#                 return False
#             node = node[char]  # 指向下一个结点
#         return '#' in node
#
#     def startsWith(self, prefix: str) -> bool:
#         node = self.root
#         for char in prefix:
#             if char not in node:
#                 return False
#             node = node[char]
#         return True

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.dic
        for c in word:
            node = node.setdefault(c, {})  # 两重意思
        node['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.dic
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.dic
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True


trie = Trie()
trie.insert("apple")
print(trie.dic)
print(trie.search("apple"))  # True

print(trie.search("app"))  # 返回 false
print(trie.startsWith("app"))  # 返回 true

trie.insert("app")
print(trie.dic)
print(trie.search("app"))
#
# print(trie.root)

# sym = ['how', 'hi', 'her', 'hello', 'so', 'see']
# for s in sym:
#     trie.insert(s)
# print(trie.dic)
#
# import pprint
# pprint.pprint(trie.dic)
