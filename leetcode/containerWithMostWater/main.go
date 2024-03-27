package main

import "fmt"

func main() {
	fmt.Println(maxArea([]int{1, 8, 6, 2, 5, 4, 8, 3, 7}))
}

func maxArea(height []int) int {
	l, r := 0, len(height)-1
	max := 0
	for l < r {
		left := height[l]
		right := height[r]

		h := min(left, right)
		w := r - l
		area := h * w
		if area > max {
			max = area
		}

		if left > right {
			r--
		} else {
			l++
		}
	}

	return max
}
