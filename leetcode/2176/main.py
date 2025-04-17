# 2176. Count Equal and Divisible Pairs in an Array
from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq = {}
        total = 0

        for i, num in enumerate(nums):
            if i in freq:
                freq[num].append(i)
            else:
                freq[num] = [i]

        for _, v in freq.items():
            if len(v) > 1:
                for i in range(len(v) - 1):
                    for j in range(i + 1, len(v)):
                        if v[i] * v[j] % 2 == 0:
                            total += 1

        return total
