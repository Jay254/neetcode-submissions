# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Iterate through the tree until you find the LCA
        while root:
            # If both p and q are smaller than the root, move to the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are larger than the root, move to the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # If p and q are on different sides of the root, or one of them equals the root
            # then the current root is the LCA
            else:
                return root