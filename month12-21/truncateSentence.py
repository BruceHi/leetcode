# 1816. 截断句子
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


obj = Solution()
s = "Hello how are you Contestant"
k = 4
print(obj.truncateSentence(s, k))

s = "What is the solution to this problem"
k = 4
print(obj.truncateSentence(s, k))

s = "chopper is not a tanuki"
k = 5
print(obj.truncateSentence(s, k))
