// 875. Koko Eating Bananas

package main

func minEatingSpeed(piles []int, h int) int {
	l, r := 1, 1
	for _, val := range piles {
		if val > r {
			r = val
		}
	}

	res := r
	for r >= l {
		mid := (r + l) >> 1
		time := divideSlice(piles, mid)
		if time <= h {
			res = min(res, mid)
			r = mid - 1
		} else {
			l = mid + 1
		}
	}

	return res
}

func divideSlice(piles []int, k int) int {
	total := 0
	for i := range len(piles) {
		if piles[i]%k == 0 {
			total += piles[i] / k
		} else {
			total += (piles[i] / k) + 1
		}
	}

	return total
}
