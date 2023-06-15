# 1161. Maximum Level Sum of a Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.levels = []

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, None, 0)
        return self.levels.index(max(self.levels)) + 1

    def dfs(self, node, visited, level):
        if visited is None:
            visited = set()
        visited.add(node)

        if level >= len(self.levels):
            self.levels.append(node.val)
        else:
            self.levels[level] += node.val

        level += 1

        if node.left is not None:
            self.dfs(node.left, visited, level)
        if node.right is not None:
            self.dfs(node.right, visited, level)

        return visited


if __name__ == "__main__":
    solver = Solution()
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(0)
    root.left.left = TreeNode(7)

    # answer should be 2
    print(solver.maxLevelSum(root))
