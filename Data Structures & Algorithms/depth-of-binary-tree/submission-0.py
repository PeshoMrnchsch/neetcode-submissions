# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        mleft = 1 + self.maxDepth(root.left)
        mright = 1 + self.maxDepth(root.right)

        if mleft >= mright:
            return mleft

        return mright