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
        count = 0
        
        while itr:
            if count == length - n - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next
        
        return head
            
        
            
            