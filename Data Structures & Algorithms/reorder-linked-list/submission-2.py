# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        #find mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        prev, cur = None, slow.next
        slow.next = None

        while cur:
            nexti = cur.next
            cur.next = prev
            prev = cur
            cur = nexti

        #merge first half and second half
        first, second = head, prev
        while first and second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2