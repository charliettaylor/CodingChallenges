# 278. First Bad Version

import math


def isBadVersion(n: int) -> bool:
    """Hard code in bad version for testing"""
    return n >= 12345


def firstBadVersion(n: int) -> int:
    if isBadVersion(1):
        return 1

    u = n
    l = 1
    while True:
        u2, l2 = u, l
        if isBadVersion((u + l) // 2):
            u = ((u + l) // 2) + 1
        else:
            l = (u + l) // 2

        if u == u2 and l == l2:
            if u - l == 1:
                return math.ceil((u + l) / 2)
            else:
                return (u + l) // 2


if __name__ == "__main__":
    print(firstBadVersion(2126753390))
