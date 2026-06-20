# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        r_tree = self.maxDepth(root.right)
        l_tree = self.maxDepth(root.left)

        return 1 + max(r_tree, l_tree)

