# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        start = preorder[0]
        root = TreeNode(start)

        root_index = inorder.index(start)

        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index+1:]

        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[1+ len(inorder_left):]

        root.left = self.buildTree(preorder_left,inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root