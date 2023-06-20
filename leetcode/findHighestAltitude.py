# 1732. Find the Highest Altitude

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x = 0
        return max([0] + [x := gain[i] + x for i in range(len(gain))])


if __name__ == "__main__":
    s = Solution()
    # should be 1
    print(s.largestAltitude([-5, 1, 5, 0, -7]))
