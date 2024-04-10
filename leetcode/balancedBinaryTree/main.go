// 110. Balanced Binary Tree

package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}

	var dfs func(root *TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}

		return max(dfs(root.Right), dfs(root.Left)) + 1
	}

	left := dfs(root.Left)
	right := dfs(root.Right)

	if abs(left-right) > 1 {
		return false
	}

	return isBalanced(root.Left) && isBalanced(root.Right)
}

func abs(i int) int {
	if i < 0 {
		return -1 * i
	} else {
		return i
	}
}
