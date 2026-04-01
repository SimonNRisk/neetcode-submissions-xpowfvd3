# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lead = dummy
        follow = dummy

        for _ in range(n+1):
            follow = follow.next

        while follow:
            lead = lead.next
            follow=follow.next
    
        lead.next = lead.next.next
        return dummy.next

        