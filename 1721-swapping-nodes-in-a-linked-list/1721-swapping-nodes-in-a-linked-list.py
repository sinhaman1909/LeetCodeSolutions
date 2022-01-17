# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        total_nodes = 0
        first_node, second_node = None, None
        ptr = head
        
        while ptr is not None:
            total_nodes += 1
            if second_node is not None:
                second_node = second_node.next
            if total_nodes == k:
                first_node = ptr
                second_node = head
            ptr = ptr.next
            
        if first_node is None:
            return head
        
        first_node.val,second_node.val = second_node.val,first_node.val
        return head
        