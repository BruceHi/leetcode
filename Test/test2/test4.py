from functools import reduce


class Solution:

    def ip_change_int(self, ips):
        def ip_to_int(ip):
            return reduce(lambda x, y: x * 1000 + y, map(int, ip.split('.')))

        res = []
        for ip in ips.split():
            ip1, ip2, _ = ip.split(',')
            res.extend([ip_to_int(ip1), ip_to_int(ip2)])
        return res



s = Solution()
ips = """0.0.0.0,1.5.7.8,CN
1.5.7.9,2.255.1.39,US
2.255.1.40,5.2.255.255,CN
123.255.1.40,5.2.255.255,CN
"""
print(ips)
print(s.ip_change_int(ips))

a = {1} | {2}
print(a)

a = 1
print('%t'.format(a))

print(ord('c')-ord('a'))

from itertools import permutations
a = [1, 2, 3]
print(list(permutations(a)))

a = [[1,1],[1,1]]
print(list(permutations(a)))
print(len(list(permutations(a))))