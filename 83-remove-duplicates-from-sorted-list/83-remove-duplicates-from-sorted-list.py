# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        appearences = []
        itr = head
        prev_itr = head
        while itr:
            if itr.val in appearences:
                prev_itr.next = itr.next
                itr = itr.next
            else:
                appearences.append(itr.val)
                prev_itr = itr
                itr = itr.next
            
        return head
                                