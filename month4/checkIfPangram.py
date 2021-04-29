# 5734. 判断句子是否为全字母句
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        judge = set('abcdefghijklmnopqrstuvwxyz')
        return set(sentence) == judge


s = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(s.checkIfPangram(sentence))

sentence = "leetcode"
print(s.checkIfPangram(sentence))
