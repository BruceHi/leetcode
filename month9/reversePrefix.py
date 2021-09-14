class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i != -1:
            return ''.join(reversed(word[:i+1])) + word[i+1:]
        return word

o = Solution()
word = "abcdefd"
ch = "d"
print(o.reversePrefix(word, ch))

word = "xyxzxe"
ch = "z"
print(o.reversePrefix(word, ch))

word = "abcd"
ch = "z"
print(o.reversePrefix(word, ch))