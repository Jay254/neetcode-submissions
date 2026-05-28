# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur = root
        parent = None
        #find node and it's parent ; cur-> node, parent -> its parent
        while cur and cur.val != key:  
            parent = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if not cur: #not found, so root is returned
            return root

        #if both left and right children exist
        if cur.left and cur.right:
            succ_parent = cur
            succ = cur.right
            while succ.left: #finding smallest of right subtree
                succ_parent = succ
                succ = succ.left

            cur.val = succ.val
            parent = succ_parent
            cur = succ

        child = cur.left if cur.left else cur.right
        if not parent:
            return child

        if parent.left == cur:
            parent.left = child
        else:
            parent.right = child

        return root
            
