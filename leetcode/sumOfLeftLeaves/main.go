// 404. Sum of Left Leaves

package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	return dfs(root, false)
}

func dfs(root *TreeNode, isLeft bool) int {
	if root == nil {
		return 0
	}

	left := dfs(root.Left, true)
	right := dfs(root.Right, false)

	if isLeft && root.Left == nil && root.Right == nil {
		return root.Val + left + right
	}

	return left + right
}
