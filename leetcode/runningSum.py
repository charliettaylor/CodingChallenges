# 1480. Running Sum of 1d Array


def runningSum(nums: list[int]) -> list[int]:
  prev = nums[0]
  for i in range(1, len(nums)):
    nums[i] += prev
    prev = nums[i]

  return nums


if __name__ == "__main__":
  # Should output [1, 3, 6, 10]
  print(runningSum([1, 2, 3, 4]))
