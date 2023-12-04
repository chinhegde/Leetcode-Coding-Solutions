# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        a, b = headA, headB
        
        while a or b:
            if a: 
                a = a.next
            else:
                headB = headB.next
            if b:
                b = b.next
            else:
                headA = headA.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        
#         a, b = headA, headB
        
#         while a and b and a!=b:
            
#             if a.next == b.next:
#                 return a.next

#             a = a.next
#             b = b.next
            
#             if not a:
#                 a = headA
            
#             if not b:
#                 b = headB
            
#         return a
        
        
            