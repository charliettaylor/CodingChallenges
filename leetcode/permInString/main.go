// 567. Permutation in String

package main

import (
	"sort"
	"strings"
)

// correct answer, thanks neetcode
func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}

	s1Hash, s2Hash := make([]int, 26), make([]int, 26)

	for i := range len(s1) {
		s1Hash[int(s1[i])-97] += 1
		s2Hash[int(s2[i])-97] += 1
	}

	matches := 0
	for i := range 26 {
		if s1Hash[i] == s2Hash[i] {
			matches += 1
		}
	}

	l := 0
	for r := len(s1); r < len(s2); r++ {
		if matches == 26 {
			return true
		}

		idx := int(s2[r]) - 97
		s2Hash[idx]++
		if s1Hash[idx] == s2Hash[idx] {
			matches++
		} else if s1Hash[idx]+1 == s2Hash[idx] {
			matches--
		}

		idx = int(s2[l]) - 97
		s2Hash[idx]--
		if s1Hash[idx] == s2Hash[idx] {
			matches++
		} else if s1Hash[idx]-1 == s2Hash[idx] {
			matches--
		}
		l++
	}

	return matches == 26
}

// my answer that timed out :(
func checkInclusionBad(s1 string, s2 string) bool {
	s1Sort := SortString(s1)
	l := 0
	for r := len(s1); r <= len(s2); r++ {
		s2Sort := SortString(s2[l:r])
		if s1Sort == s2Sort {
			return true
		}
		l++
	}

	return false
}

func SortString(w string) string {
	s := strings.Split(w, "")
	sort.Strings(s)
	return strings.Join(s, "")
}
