# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getList(root : Optional[TreeNode]) -> List:
        elements = [root.val]
        if root.left:
            elements += Solution.getList(root.left)  
        if root.right:
            elements += Solution.getList(root.right)
        return elements
            
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashmap = {}
        itr = root
        elements = Solution.getList(root)
        print(elements)
        for num in elements:
            key = k - num
            if key in hashmap:
                return True
            else:
                hashmap[num] = 1
                
        return False
           
            