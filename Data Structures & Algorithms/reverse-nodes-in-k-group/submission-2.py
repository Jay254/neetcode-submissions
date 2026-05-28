# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur and count < k:
            cur = cur.next
            count += 1

        if count < k:
            return head

        prev, cur = None, head
        for _ in range(count):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        #prev is at 3, cur is at 4, head still at 1
        head.next = self.reverseKGroup(cur, k)

        return prev