# 回复空格
from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dic = set(dictionary)
        n = len(sentence)
        dp = [0] * (n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for j in range(i):
                if sentence[j:i] in dic:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]




s = Solution()
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
print(s.respace(dictionary, sentence))