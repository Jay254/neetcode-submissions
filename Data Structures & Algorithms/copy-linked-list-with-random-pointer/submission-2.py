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
        while cur:
            orig_to_copy[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        while cur:
            orig_to_copy[cur].next = orig_to_copy.get(cur.next)
            orig_to_copy[cur].random = orig_to_copy.get(cur.random)
            cur = cur.next

        return orig_to_copy[head]