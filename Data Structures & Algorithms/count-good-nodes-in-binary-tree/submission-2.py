# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0
        def isGood(node, max_so_far):
            nonlocal count
            if not node:
                return
            if node.val >= max_so_far:
                count += 1
                max_so_far = node.val

            isGood(node.left, max_so_far)
            isGood(node.right, max_so_far)

        isGood(root, root.val)
        return count

