// 442. Find All Duplicates in an Array

package main

func findDuplicates(nums []int) []int {
	var dupes []int

	for i := range len(nums) {
		link := nums[i] - 1

		// no abs() in Go :(
		if link < 0 {
			link *= -1
			// negative got subtracted, so undo and do the opposite
			link -= 2
		}

		if nums[link] < 0 {
			if nums[i] > 0 {
				dupes = append(dupes, nums[i])
			} else {
				dupes = append(dupes, nums[i]*-1)
			}
		}
		nums[link] *= -1
	}

	return dupes
}
