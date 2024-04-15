// 153. Find Minimum in Rotated Sorted Array

package main

func findMin(nums []int) int {
	l, r := 0, len(nums)-1
	res := nums[0]
	for r >= l {
		if nums[l] < nums[r] {
			res = min(res, nums[l])
			break
		}
		m := (l + r) >> 1
		res = min(res, nums[m])

		if nums[m] >= nums[l] {
			l = m + 1
		} else {
			r = m - 1
		}
	}

	return res
}
