// 33. Search in Rotated Sorted Array

package main

func search(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for r >= l {
		mid := (l + r) >> 1

		curr := nums[mid]
		if curr == target {
			return mid
		}

		if nums[l] <= nums[mid] {
			if target > nums[mid] || target < nums[l] {
				l = mid + 1
			} else {
				r = mid - 1
			}
		} else {
			if target < nums[mid] || target > nums[r] {
				r = mid - 1
			} else {
				l = mid + 1
			}
		}
	}

	return -1
}
