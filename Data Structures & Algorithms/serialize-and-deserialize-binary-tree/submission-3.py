# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #preorder_str
        preorder =  []
        def pre_traverse(node):
            if not node:
                preorder.append('N')
                return

            preorder.append(str(node.val))

            pre_traverse(node.left)
            pre_traverse(node.right)

        pre_traverse(root)
        return ','.join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.pre = 0
        preorder = data.split(',')

        def build():
            if preorder[self.pre] == 'N':
                self.pre += 1
                return None

            node = TreeNode(int(preorder[self.pre]))
            self.pre += 1

            node.left = build()
            node.right = build()

            return node


        return build()

