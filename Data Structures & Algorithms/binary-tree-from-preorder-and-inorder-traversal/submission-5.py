# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root
        inorder_map = {node:i for i, node in enumerate(inorder)}
        pre_i = 0

        def build(l, r):
            nonlocal pre_i
            if l > r:
                return None

            root_val = preorder[pre_i]
            pre_i += 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val]
            root.left = build(l, mid-1)
            root.right = build(mid+1, r)

            return root

        return build(0, len(preorder)-1)



