# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:   
        if head is None:
            return
        
        if head.next is None:
            return head
        
        n, tail = 1, head

        while tail.next:
            tail = tail.next
            n += 1

        k = k % n

        if k == 0:
            return head
        
        rotations = 0
        while rotations < k:
            itr = head.next
            prev = head
            while itr.next:
                prev = prev.next
                itr = itr.next
            rotations += 1
            prev.next = None
            itr.next = head
            head = itr

        return head
            