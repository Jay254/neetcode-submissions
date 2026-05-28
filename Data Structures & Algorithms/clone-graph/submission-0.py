"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        # Dictionary to keep track of cloned nodes
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        # If the input node is None, return None
        if not node:
            return None

        # If the node has already been cloned, return its clone
        if node in self.visited:
            return self.visited[node]

        # Create a clone for the current node (without neighbors for now)
        clone_node = Node(node.val, [])

        # Mark this node as visited by adding it to the visited dictionary
        self.visited[node] = clone_node

        # Clone all the neighbors recursively
        for neighbor in node.neighbors:
            # Append the cloned neighbors to the current cloned node
            clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node