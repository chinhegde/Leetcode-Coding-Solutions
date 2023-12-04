# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        stk = list()

        while head:
            stk.append(head.val)
            head = head.next

        if stk == stk[::-1]: return True
        else: return False

        