# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        itr = head
        
        while itr.next:
            length += 1
            itr = itr.next
            
        delete_index = length//2
        
        if delete_index == 0:
            head = head.next
            return head
        
        itr = head
        for i in range(delete_index - 1):
            itr = itr.next
            
        itr.next = itr.next.next
        
        return head