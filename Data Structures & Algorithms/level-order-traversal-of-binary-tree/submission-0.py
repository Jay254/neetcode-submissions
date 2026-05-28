# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS traversal -> queue
        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize queue with root node

        while queue:
            level_size = len(queue)  # Number of nodes in the current level
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()  # Dequeue node
                current_level.append(node.val)  # Add node value to current level

                if node.left:
                    queue.append(node.left)  # Enqueue left child
                if node.right:
                    queue.append(node.right)  # Enqueue right child

            result.append(current_level)  # Add current level to result

        return result