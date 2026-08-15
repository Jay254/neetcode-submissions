# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)
        before = dummy

        for _ in range(left - 1):
            before = before.next

        prev = None
        cur = before.next

        for _ in range(right - left + 1):
            nexti = cur.next
            cur.next = prev
            prev = cur
            cur = nexti

        before.next.next = cur
        before.next = prev

        return dummy.next

