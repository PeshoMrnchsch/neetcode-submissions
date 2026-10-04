# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        
        def dep(root:Optional[TreeNode], depth:int):
            if not root:
                return
            if depth == len(res):
                res.append([])
            
            res[depth].append(root.val)
            dep(root.left, depth + 1)
            dep(root.right, depth + 1)

        dep(root, 0)
        return res