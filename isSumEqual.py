class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def str_sum(s):
            res = 0
            for c in s:
                res = res * 10 + ord(c) - ord('a')
            return res
        return str_sum(firstWord) + str_sum(secondWord) == str_sum(targetWord)


s = Solution()
firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(s.isSumEqual(firstWord, secondWord, targetWord))

firstWord = "aaa"
secondWord = "a"
targetWord = "aab"
print(s.isSumEqual(firstWord, secondWord, targetWord))


firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
print(s.isSumEqual(firstWord, secondWord, targetWord))

firstWord = "j"
secondWord = "j"
targetWord = "bi"
print(s.isSumEqual(firstWord, secondWord, targetWord))

