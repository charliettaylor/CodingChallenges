// 1046. Last Stone Weight

package main

import "sort"

func lastStoneWeight(stones []int) int {
	sort.Slice(stones, func(i, j int) bool {
		return stones[i] > stones[j]
	})

	for len(stones) > 1 {
		l, r := stones[0], stones[1]

		if len(stones) <= 2 {
			stones = make([]int, 0)
		} else {
			stones = stones[2:]
		}

		if abs(l-r) != 0 {
			stones = append(stones, abs(l-r))
		}

		sort.Slice(stones, func(i, j int) bool {
			return stones[i] > stones[j]
		})
	}

	if len(stones) != 0 {
		return stones[0]
	} else {
		return 0
	}
}

func abs(num int) int {
	if num < 0 {
		return num * -1
	} else {
		return num
	}
}
