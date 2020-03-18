from collections import Counter


def isAnagram(s, t):
    return Counter(s) == Counter(t)


# 排序
def isAnagram(s, t):
    return sorted(s) == sorted(t)

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))

s = "rat"
t = "car"
print(isAnagram(s, t))
