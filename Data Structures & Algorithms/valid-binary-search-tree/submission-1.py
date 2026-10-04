# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # calling left = setting max limit
        # calling right  = setting min limit

        def helper(root: Optional[TreeNode], minVal, maxVal) -> bool:
            if not root:
                return True
            
            if root.val > minVal and root.val < maxVal:
                l = helper(root=root.left, minVal= minVal, maxVal= root.val)
                r = helper(root=root.right, minVal= root.val, maxVal= maxVal)
                if l and r:
                    return True
            return False

        res = helper(root=root, minVal= float('-inf'), maxVal = float('inf'))
        return res

            

            