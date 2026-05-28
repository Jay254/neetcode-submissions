# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable to track the maximum path sum
        # Since node values can be negative, we set it to a very small number.
        self.max_sum = float('-inf')

        # Helper function to calculate the maximum sum of paths that pass through each node
        def max_gain(node):
            if not node:
                # If we reach a null node, return 0 because null nodes do not contribute to the path sum
                return 0

            # Recursively calculate the maximum sum from the left and right subtrees
            # We only consider positive gains, because if a subtree gives a negative sum, 
            # it's better to not include it in the path.
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # The price to start a new path where `node` is the highest node (the root of this path)
            new_path_sum = node.val + left_gain + right_gain

            # Update the global max_sum if the new path_sum is larger than the current max_sum
            self.max_sum = max(self.max_sum, new_path_sum)

            # Return the maximum gain if we continue the same path (i.e., the path that uses `node` and one of its subtrees)
            # We return the value of node plus the maximum gain from either the left or right subtree
            return node.val + max(left_gain, right_gain)

        # Start the recursive process from the root
        max_gain(root)

        # Return the maximum path sum found
        return self.max_sum
