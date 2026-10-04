# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder tree
        state ={
            "count" : 0, 
            "answer":0
        }
        def inorder(node: Optional[TreeNode]):
            if not node:
                return
            
            inorder(node.left)
            state["count"]+=1
            if state["count"] == k:
                state["answer"] = node.val
            
            inorder(node.right)

        inorder(root)
        return state["answer"]
