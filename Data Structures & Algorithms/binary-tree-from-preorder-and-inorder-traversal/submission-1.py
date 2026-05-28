# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            # If either list is empty, no more nodes can be constructed
            return None
        
        # Step 1: The first element of preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Step 2: Find the index of the root in the inorder list
        root_index = inorder.index(root_val)

        # Step 3: Split inorder into left and right subtrees
        inorder_left = inorder[:root_index]
        inorder_right = inorder[root_index + 1:]

        # Step 4: Split preorder into left and right parts based on the size of inorder's left part
        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        # Step 5: Recursively build the left and right subtrees
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        # Return the constructed tree node
        return root