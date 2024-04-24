// 1137. N-th Tribonacci Number

package main

func tribonacci(n int) int {
	list := []int{0, 1, 1}

	for i := 2; i < n; i++ {
		list = append(list, list[i]+list[i-1]+list[i-2])
	}

	return list[n]
}
