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

        cur = head
        old_new = {}

        while cur:
            old_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            if cur.next:
                old_new[cur].next = old_new[cur.next]
            if cur.random:
                old_new[cur].random = old_new[cur.random]

            cur = cur.next

        return old_new[head]
