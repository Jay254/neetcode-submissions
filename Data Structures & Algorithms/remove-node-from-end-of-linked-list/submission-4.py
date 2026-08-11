# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        for _ in range(n):
            cur = cur.next

        prev = dummy
        
        while cur.next:
            prev = prev.next
            cur = cur.next

        prev.next = prev.next.next

        return dummy.next