# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        prev = None

        #[0,1,2,3]
        while cur:
            next_node = cur.next #1,2,3
            cur.next = prev # None
            prev = cur # 0
            cur = next_node

        return prev
