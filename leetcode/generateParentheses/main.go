package main

import "fmt"

func main() {
	fmt.Println(generateParenthesis(3))
}

func generateParenthesis(n int) []string {
	stack := make([]string, 0)
	res := make([]string, 0)

	var backtrack func(open, close int)
	backtrack = func(open, close int) {
		if open == close && close == n {
			res = append(res, joinStack(stack))
			return
		}

		if open < n {
			stack = append(stack, "(")
			backtrack(open+1, close)
			stack = stack[:len(stack)-1]
		}

		if close < open {
			stack = append(stack, ")")
			backtrack(open, close+1)
			stack = stack[:len(stack)-1]
		}
	}

	backtrack(0, 0)
	return res
}

func joinStack(stack []string) string {
	var j string
	for _, c := range stack {
		j = j + c
	}

	return j
}
