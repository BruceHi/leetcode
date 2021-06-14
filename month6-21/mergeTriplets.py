from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True
        x, y, z = [], [], []
        for i, (a, b, c) in enumerate(triplets):
            if a == target[0]:
                x.append(i)
            if b == target[1]:
                y.append(i)
            if c == target[2]:
                z.append(i)
        if not x or not y or not z:
            return False
        for i in range(len(x)):
            for j in range(len(y)):
                for k in range(len(z)):
                    if [max(triplets[x[i]][0], triplets[y[j]][0], triplets[z[k]][0]),
                        max(triplets[x[i]][1], triplets[y[j]][1], triplets[z[k]][1]),
                        max(triplets[x[i]][2], triplets[y[j]][2], triplets[z[k]][2])] == target:
                        return True
        return False



s = Solution()
triplets = [[2,5,3],[1,8,4],[1,7,5]]
target = [2,7,5]
print(s.mergeTriplets(triplets, target))

triplets = [[1,3,4],[2,5,8]]
target = [2,5,8]
print(s.mergeTriplets(triplets, target))

triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
target = [5,5,5]
print(s.mergeTriplets(triplets, target))

triplets = [[3,4,5],[4,5,6]]
target = [3,2,5]
print(s.mergeTriplets(triplets, target))

triplets = [[2, 7, 3], [3, 2, 8]]
target = [2, 7, 8]
print(s.mergeTriplets(triplets, target))
