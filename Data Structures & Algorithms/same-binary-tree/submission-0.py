# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        arr1 = []
        arr2 = []
        def tree_arr(node, arr):
            if not node:
                return
            arr.append(node.val)
            left = tree_arr(node.left, arr)
            right = tree_arr(node.right, arr)
        
        tree_arr(p, arr1)
        tree_arr(q, arr2)
        print(arr1)
        print(arr2)

        return arr1 == arr2