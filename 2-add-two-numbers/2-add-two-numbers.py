# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        num1 = ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
            
        
        cur2 = l2
        num2 = ""
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        print(num1, num2)
        num1 = int(num1)
        num2 = int(num2)
        print(num1, num2)

        
        res = str(num1 + num2)
        print(res)
        
        newHead = ListNode(int(res[-1]))
        itr = newHead
        
        for i in range(len(res)-2,-1,-1):
            itr.next = ListNode(int(res[i]))
            itr = itr.next
        
        return newHead
        