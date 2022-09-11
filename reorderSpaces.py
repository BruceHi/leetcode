# 1529. 重新排列单词间的空格
import math


class Solution:
    # def reorderSpaces(self, text: str) -> str:
    #     words = text.split()
    #     words_len = len(words)
    #     # space_len = len([x for x in text if x == ' '])
    #     space_len = text.count(' ')
    #
    #     if words_len == 1:
    #         return words[0] + ' ' * space_len
    #
    #     space, end = divmod(space_len, words_len-1)
    #     return (' ' * space).join(words) + ' ' * end

    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        words_count = len(words)
        count = text.count(' ')

        if words_count == 1:
            return words[0] + ' ' * count

        remain_space, remain_end = divmod(count, words_count-1)

        return (' '*remain_space).join(words) + ' ' * remain_end



s = Solution()
text = "  this   is  a sentence "
print(s.reorderSpaces(text))

text = " practice   makes   perfect"
print(s.reorderSpaces(text))

text = "hello   world"
print(s.reorderSpaces(text))

text = "  walks  udp package   into  bar a"
print(s.reorderSpaces(text))

text = "a"
print(s.reorderSpaces(text))

text = "  hello"
print(s.reorderSpaces(text))

