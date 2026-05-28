# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # (rob, skip)
        def dfs(node):
            if not node:
                return (0,0) # if you rob or skip it, = 0

            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1] #rob this node, and skip their children

            best_from_left = max(left[0], left[1]) #if you rob or skip left child
            best_from_right = max(right[0], right[1]) #if you rob or skip right child

            skip = best_from_left + best_from_right

            return (rob,skip)



        rob, skip = dfs(root)

        return max(rob, skip)