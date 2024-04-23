// 28. Find the Index of the First Occurrence in a String

package main

func strStr(haystack string, needle string) int {
	for i := range len(haystack) - len(needle) + 1 {
		if haystack[i:i+len(needle)] == needle {
			return i
		}
	}

	return -1
}