// 704. Binary Search

package main

func search(nums []int, target int) int {
	min, max := 0, len(nums)-1

	for max >= min {
		// using bit shift 🧠
		mid := (min + max) >> 1
		if target == nums[mid] {
			return mid
		} else if target < nums[mid] {
			max = mid - 1
		} else {
			min = mid + 1
		}
	}

	return -1
}
