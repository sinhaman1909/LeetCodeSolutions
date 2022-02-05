# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return 
        
        nums = []
        for head in lists:
            if head:
                itr = head
                while itr:
                    nums.append(itr.val)
                    itr = itr.next
            else:
                continue
                
        if len(nums) == 0:
            return
        
        nums = sorted(nums)
        newHead = ListNode()
        itr = newHead
        for i,num in enumerate(nums):
            itr.val = num
            if i != len(nums) - 1: 
                itr.next = ListNode()
            itr = itr.next
            
        return newHead