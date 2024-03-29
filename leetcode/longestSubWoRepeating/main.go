// 3. Longest Substring Without Repeating Characters

package main

// first attempt
func lengthOfLongestSubstring(s string) int {
	l, r, long := 0, 0, 0
	for r < len(s) {
		curr := s[l : r+1]
		if unique(curr) && len(curr) > long {
			long = len(curr)
		} else {
			l++
		}
		r++
	}

	return long
}

func unique(arr string) bool {
	m := make(map[rune]bool)
	for _, i := range arr {
		if _, ok := m[i]; ok {
			return false
		}

		m[i] = true
	}
	return true
}

// use a set like neetcode
func lengthOfLongestSubstringSet(s string) int {
	l, long := 0, 0
	m := make(map[byte]bool)
	for r := range s {
		_, in := m[s[r]]
		for in {
			delete(m, s[l])
			l++
			in = m[s[r]]
		}
		m[s[r]] = true
		long = max(long, r-l+1)
	}

	return long
}
