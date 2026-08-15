# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        cur_parent = None
        while cur:
            cur_parent = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        if val < cur_parent.val:
            cur_parent.left = TreeNode(val)
        else:
            cur_parent.right = TreeNode(val)

        return root