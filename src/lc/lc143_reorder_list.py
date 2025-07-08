# Leetcode 143. Reorder List
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None: return

        i = 0
        current = head
        dic = {}
        while current:
            dic[i] = current
            current = current.next
            i += 1
        # i is now the length of the linked list e.g list[i] is out of bounds

        for di in range(0, i//2):
            a = dic.get(di)
            b = dic.get(i-di-1) # i - 1 is the last index 
            c = dic.get(di+1)
            if a and b:
                a.next = b
                b.next = None
            if b and c: 
                b.next = c
                c.next = None
                
        

        