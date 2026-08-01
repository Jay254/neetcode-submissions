# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        def isSub(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return isSub(p.left, q.left) and isSub(p.right, q.right)

        def traverse(node):
            if not node:
                return False
            if node.val == subRoot.val and isSub(node, subRoot):
                return True
            
            return traverse(node.left) or traverse(node.right)

        return traverse(root)


        