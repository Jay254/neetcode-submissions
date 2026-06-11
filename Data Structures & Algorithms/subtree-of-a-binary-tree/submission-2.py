# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        def traverse(node):
            if not node:
                return False

            if node.val == subRoot.val:
                if isSame(node, subRoot):
                    return True

            left = traverse(node.left)
            right = traverse(node.right)

            if left or right:
                return True

            return False

        return traverse(root)