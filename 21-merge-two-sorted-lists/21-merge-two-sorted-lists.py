# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertValue(data, head):
        if head is None:
            head = ListNode(data, None)
            return
        
        else:
            itr = head
            while itr.next:
                itr = itr.next

            itr.next = ListNode(data, None)
            
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        itr1 = list1
        itr2 = list2
        data_list = []
        head = ListNode()
        
        while itr1:
            data_list.append(itr1.val)
            itr1 = itr1.next
            
        while itr2:
            data_list.append(itr2.val)
            itr2 = itr2.next
        
        data_list.sort()
        
        for data in data_list:
            Solution.insertValue(data, head)
            
        return head.next
        
            
        
            
        
        