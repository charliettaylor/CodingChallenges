# 268. Missing Number


def missingNumber(nums: list[int]) -> int:
    n = max(nums)
    total = int(n * ((n + 1) / 2)) - sum(nums)

    return total if total != 0 or 0 not in nums else n + 1


if __name__ == "__main__":
    print(missingNumber([3, 0, 1]))
