// 853. Car Fleet

package main

import (
	"sort"
)

func carFleet(target int, position []int, speed []int) int {
	if len(position) == 1 {
		return 1
	}

	// zip slices
	cars := make([][]int, 0)
	for i := range len(position) {
		cars = append(cars, []int{position[i], speed[i]})
	}

	// sort by reversed position
	sort.Slice(cars, func(i, j int) bool {
		return cars[i][0] > cars[j][0]
	})

	stack := make([]float64, 0)
	for _, car := range cars {
		stack = append(stack, float64(target-car[0])/float64(car[1]))
		if len(stack) >= 2 && stack[len(stack)-1] <= stack[len(stack)-2] {
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack)
}
