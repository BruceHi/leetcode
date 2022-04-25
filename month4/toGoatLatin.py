# 824. 山羊拉丁文
class Solution:
    # def toGoatLatin(self, sentence: str) -> str:
    #     vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    #     res = []
    #     for i, sent in enumerate(sentence.split()):
    #         c = sent
    #         if sent[0] not in vowel:
    #             c = sent[1:] + sent[0]
    #         c += 'ma' + 'a' * (i+1)
    #         res.append(c)
    #     return ' '.join(res)

    def toGoatLatin(self, sentence: str) -> str:
        res = []
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for i, sent in enumerate(sentence.split()):
            t = sent
            if t[0] not in vowel:
                t = sent[1:] + sent[0]
            res.append(t + 'ma' + 'a' * (i+1))
        return ' '.join(res)


s = Solution()
sentence = "I speak Goat Latin"
print(s.toGoatLatin(sentence))

sentence = "The quick brown fox jumped over the lazy dog"
print(s.toGoatLatin(sentence))
