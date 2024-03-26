// 15. 3Sum

package main

import "slices"

func threeSum(nums []int) [][]int {
	var trips [][]int
	slices.Sort(nums)

	for i, a := range nums {
		if i > 0 && a == nums[i-1] {
			continue
		}

		l, r := i+1, len(nums)-1
		for l < r {
			threeSum := nums[i] + nums[l] + nums[r]
			if threeSum > 0 {
				r--
			} else if threeSum < 0 {
				l++
			} else {
				trips = append(trips, []int{nums[i], nums[l], nums[r]})
				l++
				for nums[l] == nums[l-1] && l < r {
					l++
				}
			}
		}
	}

	return trips
}
