# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res=[]

        def helper(root: Optional[TreeNode], dep:int):
            if not root:
                return
            
            if dep == len(res):
                res.append(root.val)
            elif root.val > res[dep]:
                res[dep] = root.val

            helper(root.left, dep+1)
            helper(root.right, dep+1)
        
        helper(root, 0)
        return res