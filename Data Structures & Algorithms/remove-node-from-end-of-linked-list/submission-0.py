# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if n == len()
        dummy = ListNode(0,head)
        slow = dummy
        fast = head

        steps = 0
        while steps < n:
            fast = fast.next
            steps += 1
        
        while fast:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next

        return dummy.next


