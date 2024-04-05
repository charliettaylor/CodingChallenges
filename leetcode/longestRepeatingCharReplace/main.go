// 424. Longest Repeating Character Replacement

package main

func characterReplacement(s string, k int) int {
	count := make(map[byte]int)
	res := 0

	maxFreq := func() int {
		max := 0
		for _, v := range count {
			if v > max {
				max = v
			}
		}

		return max
	}

	l := 0
	for r := range len(s) {
		_, ok := count[s[r]]
		if ok {
			count[s[r]] += 1
		} else {
			count[s[r]] = 1
		}

		winLength := r - l + 1
		if winLength-maxFreq() <= k {
			if winLength > res {
				res = winLength
			}
		} else {
			count[s[l]] -= 1
			l++
		}
	}

	return res
}

// use maxf to get rid of O(26) lookup
func characterReplacementWithOptimization(s string, k int) int {
	count := make(map[byte]int)
	res, l, maxf := 0, 0, 0

	for r := range len(s) {
		_, ok := count[s[r]]
		if ok {
			count[s[r]] += 1
		} else {
			count[s[r]] = 1
		}
		maxf = max(maxf, count[s[r]])

		for r-l+1-maxf > k {
			count[s[l]] -= 1
			l++
		}

		res = max(r-l+1, res)
	}

	return res
}
