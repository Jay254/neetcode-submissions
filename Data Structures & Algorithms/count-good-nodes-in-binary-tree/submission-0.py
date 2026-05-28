# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curMax):
            if not node:
                return 0

            good = 1 if node.val >= curMax else 0

            newMax = max(node.val, curMax)

            good += dfs(node.left, newMax)
            good += dfs(node.right, newMax)

            return good

        return dfs(root, root.val)


        