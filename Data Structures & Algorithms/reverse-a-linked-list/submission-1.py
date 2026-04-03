# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # each node has val and next
        # have two pointers, curr and prev
        # curr's next stored in prev
        # curr's next changed to null for the start
        # prev next change to curr
        # after start
        if not head:
            return None
        prev = None
        while head and head.next:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        head.next = prev
        return head
        