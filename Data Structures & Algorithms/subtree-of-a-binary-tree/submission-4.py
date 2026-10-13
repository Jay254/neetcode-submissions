# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSubTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return isSubTree(p.left, q.left) and isSubTree(p.right, q.right)

        def traverse(node):
            if not node:
                return False

            if isSubTree(node, subRoot):
                return True

            return traverse(node.left) or traverse(node.right)

        return traverse(root)