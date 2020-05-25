# 实现字典树
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.setdefault(char, {})  # 遍历结束时，node 指向的是 {}
        node['#'] = '#'

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]  # 指向下一个结点
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


trie = Trie()
trie.insert("apple")
print(trie.root)
print(trie.search("apple"))  # True

print(trie.search("app"))  # 返回 false
print(trie.startsWith("app"))  # 返回 true

trie.insert("app")
print(trie.search("app"))

print(trie.root)
