# 2843. Count Symmetric Integers


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        total = 0

        def isSymmetric(num: int):
            left, right = 0, 0
            snum = str(num)
            if len(snum) % 2 != 0:
                return False

            for i, curr in enumerate(snum):
                if i < len(snum) // 2:
                    left += int(curr)
                else:
                    right += int(curr)

            return left == right

        for i in range(low, high):
            if isSymmetric(i):
                total += 1

        return total
