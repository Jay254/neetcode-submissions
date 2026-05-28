# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # This will store the maximum diameter found

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Base case: height of an empty node is 0

            # Recursively calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # The diameter at the current node is the sum of left and right subtree heights
            current_diameter = left_height + right_height
            # Update the maximum diameter if the current one is larger
            self.diameter = max(self.diameter, current_diameter)

            # Return the height of the tree rooted at this node
            return 1 + max(left_height, right_height)

        height(root)  # Start the recursive height calculation from the root
        return self.diameter