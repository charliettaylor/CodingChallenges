// 100. Same Tree

package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil || q == nil {
		return p == q
	}

	var solve func(left *TreeNode, right *TreeNode) bool
	solve = func(left *TreeNode, right *TreeNode) bool {
		if left == nil || right == nil {
			return left == right
		}

		if left.Val != right.Val {
			return false
		}

		return solve(left.Left, right.Left) && solve(left.Right, right.Right)
	}

	return p.Val == q.Val && solve(p.Left, q.Left) && solve(p.Right, q.Right)
}

// cleaner not dumb solution
func isSameTreeImproved(p *TreeNode, q *TreeNode) bool {
    if p == nil || q == nil {
        return p == q
    }

	if p.Val != q.Val {
		return false
	}

	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}