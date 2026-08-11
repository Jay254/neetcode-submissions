"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        orig_to_copy = {}
        cur = head

        #copy of every node
        while cur:
            orig_to_copy[cur] = Node(cur.val)
            cur = cur.next

        #now apply their next and random references
        node = head
        for node in orig_to_copy:
            if node.next:
                orig_to_copy[node].next = orig_to_copy[node.next]
            if node.random:
                orig_to_copy[node].random = orig_to_copy[node.random]
            node = node.next

        return orig_to_copy[head]
