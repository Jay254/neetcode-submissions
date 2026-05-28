# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "[]"  # Return empty brackets if the tree is empty

        queue = deque([root])  # Initialize a queue with the root node
        result = []

        while queue:
            node = queue.popleft()  # Get the front node in the queue
            if node:
                result.append(str(node.val))  # Append the node value
                queue.append(node.left)  # Add the left child to the queue
                queue.append(node.right)  # Add the right child to the queue
            else:
                result.append("null")  # Use "null" to denote absent nodes
        
        # Remove trailing "null" values for cleaner output
        while result and result[-1] == "null":
            result.pop()

        return "[" + ",".join(result) + "]"  # Format result as a list string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "[]":
            return None  # Return None if the input is an empty list

        # Split the input string and convert to a queue of values
        values = data[1:-1].split(",")
        root = TreeNode(int(values[0]))  # The first value is the root
        queue = deque([root])  # Initialize a queue with the root node

        index = 1  # Start index for left and right children

        while queue:
            node = queue.popleft()  # Get the front node in the queue

            # Assign the left child
            if index < len(values) and values[index] != "null":  # Check index bounds
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)  # Add left child to queue
            index += 1  # Move to the next value

            # Assign the right child
            if index < len(values) and values[index] != "null":  # Check index bounds
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)  # Add right child to queue
            index += 1  # Move to the next value

        return root  # Return the root of the reconstructed tree