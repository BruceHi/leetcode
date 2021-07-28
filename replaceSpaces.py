class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")


obj = Solution()
S = "Mr John Smith    "
length = 13
print(obj.replaceSpaces(S, length))

S = "               "
length = 5
print(obj.replaceSpaces(S, length))
