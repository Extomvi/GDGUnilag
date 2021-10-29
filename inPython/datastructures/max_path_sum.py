"""Binary Tree Maximum Path Sum"""

'''
Given a non-binary binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node from some starting node to any node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.
'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maximumPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.dfs(root)[1]
    def dfs(self, node):
        if node is None:
            return(-float('inf'), -float('inf'))
        leftbranch = self.dfs(node.left)
        rightbranch = self.dfs(node.right)
        current_sum = max(leftbranch[0] + node.val, node.val + rightbranch[0], node.val)
        return (current_sum,  max(current_sum, leftbranch[1], rightbranch[1], leftbranch[0] + rightbranch[0] + node.val))

