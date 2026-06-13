# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def traverse(node):
            if not node:
                return 0

            left_sum = max(traverse(node.left), 0)
            right_sum = max(traverse(node.right), 0)

            self.max_sum = max(self.max_sum, left_sum + node.val + right_sum)
            
            return node.val + max(left_sum, right_sum)
            

        return max(traverse(root), self.max_sum)