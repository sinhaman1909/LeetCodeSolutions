# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        itr = head
        
        while itr.next:
            length += 1
            itr = itr.next
        
        if length - n == 0:
            head = head.next
            return head
            
        itr = head
        for i in range(length - n - 1): 
            itr = itr.next
            
        itr.next = itr.next.next
        
        return head
            
        
            
            