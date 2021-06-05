import re


class Solution:

    def camel_to_under(self, s):
        s1 = re.sub(r'(.)([A-Z][a-z\d])', r'\1_\2', s)  # 分离 正确的构造: 大写 + 小写（数字）
        return re.sub(r'([a-z\d])([A-Z])', r'\1_\2', s1).lower()


obj = Solution()
s = 'myFirstName'
print(obj.camel_to_under(s))

s = 'OnlineUsers'
print(obj.camel_to_under(s))

s = 'Address'
print(obj.camel_to_under(s))

s = 'validHTTPRequest'
print(obj.camel_to_under(s))

s = 'validHTTPRequestHTTP'
print(obj.camel_to_under(s))

s = 'validHTTPRequestHTTPRequestHTTP'
print(obj.camel_to_under(s))
