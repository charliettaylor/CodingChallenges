// 543. Diameter of Binary Tree

package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	diameter := 0

	var dfs func(*TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		l, r := dfs(node.Left), dfs(node.Right)
		diameter = max(diameter, l+r)

		return max(l, r) + 1
	}

	dfs(root)
	return diameter
}
