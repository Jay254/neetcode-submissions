# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Helper function to validate the BST with bounds
        def validate(node, low, high):
            # If we reach a None node, it's valid by default (base case)
            if not node:
                return True
            
            # The current node's value must be within the range (low, high)
            if not (low < node.val < high):
                return False

            # Recursively validate the left subtree and right subtree
            # Left subtree: All values must be less than the current node's value (node.val)
            # Right subtree: All values must be greater than the current node's value (node.val)
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        # Initially, the range is (-infinity, +infinity)
        return validate(root, float('-inf'), float('inf'))
