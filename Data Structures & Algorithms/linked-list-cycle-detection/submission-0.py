# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        cur = head
        n = head.next
        while n is not None:
            if cur== n:
                return True
            if cur.next is not None:
                cur = cur.next
            else:
                return False
            if n.next is not None and n.next.next is not None:
                n = n.next.next
            else:
                return False
            
        return False
        
        
        