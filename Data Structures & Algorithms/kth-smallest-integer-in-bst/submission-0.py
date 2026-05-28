# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def in_order_traversal(node):
            if not node:
                return None

            in_order_traversal(node.left)
            arr.append(node.val)
            in_order_traversal(node.right)

        in_order_traversal(root)

        return arr[k-1]
        #print(arr)