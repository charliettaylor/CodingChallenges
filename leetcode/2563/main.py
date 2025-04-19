# 2563. Count the Number of Fair Pairs
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1
        total = 0

        # get all fair pairs under upper
        while left < right:
            if nums[left] + nums[right] <= upper:
                total += right - left
                left += 1
            else:
                right -= 1

        left, right = 0, len(nums) - 1

        # removes fair pairs under lower
        while left < right:
            if nums[left] + nums[right] < lower:
                total -= right - left
                left += 1
            else:
                right -= 1

        return total
