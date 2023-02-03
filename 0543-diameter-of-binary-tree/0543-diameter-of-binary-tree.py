# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def diameterOfBinaryTreeHelp(root):
        
            if root is None:
                return 0,0

            ldia, lh = diameterOfBinaryTreeHelp(root.left)
            rdia, rh = diameterOfBinaryTreeHelp(root.right)

            dia = max(lh+rh,ldia,rdia)
            height = 1 + max(lh,rh)

            return dia,height
        
        dia, height = diameterOfBinaryTreeHelp(root)
        
        return dia
        
        
        
        
        
        
        