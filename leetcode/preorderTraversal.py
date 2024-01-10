# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited = [root]
        path = []

        while len(visited) > 0 and visited[0] != None:
            curr = visited.pop()
            path.append(curr.val)

            if curr.right != None:
                visited.append(curr.right)

            if curr.left != None:
                visited.append(curr.left)
        
        return path
