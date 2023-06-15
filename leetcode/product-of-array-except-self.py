# 238: Product of Array Except Self


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        last = 1

        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]

        for i in range(len(nums))[::-1]:
            result[i] *= last
            last *= nums[i]

        return result
