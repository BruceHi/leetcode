from typing import List
from operator import floordiv


class Solution:
    # def storeWater(self, bucket: List[int], vat: List[int]) -> int:
    #     max_value = max(bucket)
    #     idx = bucket.index(max_value)
    #     if vat[idx] % max_value:
    #         k = vat[idx] // max_value + 1
    #     else:
    #         k = vat[idx] // max_value
    #     min_val = min(bucket)
    #     min_idx = bucket.index(min_val)
    #     if min_val * k >= vat[min_idx]:
    #         return k
    #     if (min_val+1) * k >= vat[min_idx]:
    #         return k+1

    # def storeWater(self, bucket: List[int], vat: List[int]) -> int:
    #     # min_val, max_val = float('inf'), float('-inf')
    #     # for i in range(len(bucket)):
    #     #     if bucket[i] < vat[i]:
    #     min_bucket, max_bucket = float('inf'), float('-inf')
    #     min_vat, max_vat = float('inf'), float('-inf')
    #     for b, v in zip(bucket, vat):
    #         if v > b:
    #             if b < min_bucket:
    #                 min_bucket, min_vat = b, v
    #             if b > max_bucket:
    #                 max_bucket, max_vat = b, v
    #     if max_vat % max_bucket:
    #         k = max_vat // max_bucket + 1
    #     else:
    #         k = max_vat // max_bucket
    #     if min_bucket * k >= min_vat:
    #         return k
    #     if (min_bucket+1) * k >= min_vat:
    #         return k+1

    # def storeWater(self, bucket: List[int], vat: List[int]) -> int:
    #     k = 0
    #     b1, v1 = 0, 0
    #     zero = 0
    #     # 记录差值最大的k值
    #     for b, v in zip(bucket, vat):
    #         if v != 0:
    #             if b == 0:
    #                 zero += 1
    #                 b += 1
    #             tmp = v//b + 1 if v%b else v // b
    #
    #             if tmp + zero > k:
    #                 k = tmp + zero
    #                 b1, v1 = b, v
    #
    #     new = k
    #     i = 1
    #     while True:
    #         tmp = v1 // (b1 + i) + 1 if v1 % (b1 + i) else v1 // (b1 + i)
    #         if tmp + zero + i < k:
    #             k = new
    #             new = tmp + zero + i
    #             i += 1
    #         else:
    #             break
    #
    #     return new

    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        k = 0
        b1, v1 = 0, 0
        zero = 0
        # 记录差值最大的k值
        for b, v in zip(bucket, vat):
            if v != 0:
                if b == 0:
                    zero += 1
                    b += 1
                tmp = v//b + 1 if v%b else v // b

                if tmp + zero > k:
                    k = tmp + zero
                    b1, v1 = b, v

        new = k
        i = 1
        while True:
            tmp = v1 // (b1 + i) + 1 if v1 % (b1 + i) else v1 // (b1 + i)
            if tmp + zero + i < k:
                k = new
                new = tmp + zero + i
                i += 1
            else:
                break

        return new


s = Solution()
bucket = [1,3]
vat = [6,8]
print(s.storeWater(bucket, vat))

bucket = [9,0,1]
vat = [0,2,2]
print(s.storeWater(bucket, vat))

bucket = [0]
vat = [0]
print(s.storeWater(bucket, vat))

bucket = [0, 2, 8]
vat = [0, 1, 0]
print(s.storeWater(bucket, vat))

bucket = [1, 0, 8]
vat = [2, 1, 19]
print(s.storeWater(bucket, vat))

bucket = [1, 1, 1]
vat = [2, 1, 19]
print(s.storeWater(bucket, vat))

bucket = [0, 1]
vat = [0, 0]
print(s.storeWater(bucket, vat))

bucket = [2, 4]
vat = [2, 5]
print(s.storeWater(bucket, vat))