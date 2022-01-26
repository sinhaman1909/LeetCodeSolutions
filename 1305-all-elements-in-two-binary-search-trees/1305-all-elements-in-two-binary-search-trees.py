# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(root: TreeNode) -> List[int]:
        elements = []
        if root is None:
            return []
        if root.left:
            elements += Solution.inorder(root.left)
        elements.append(root.val)
        
        if root.right:
            elements += Solution.inorder(root.right)
            
        return elements
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        elements = Solution.inorder(root1)
        elements += Solution.inorder(root2)
        return sorted(elements)
        