# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #constant space and O(N) time for fast slow tortoise hare
        slow = head
        fast = head.next
        #while head.next and head.next.next
        while fast and fast.next:
            if (slow == fast):
                return True
            fast = fast.next.next
            slow = slow.next
        return False