# Leetcode 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = ListNode(0, None)

        prev = pointer
        current = head
        while current:
            if not current.next or current.next.val != current.val:
                prev.next = current
                prev = current
            else:
                while current.next and current.next.val == current.val:
                    current = current.next
            current = current.next
        prev.next = None # Must trim off end in case last was a duplicate
        return pointer.next
    
# See Also: LC80

# First Solution:
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        stack = [head] # Stack is overkill but works
        current = head.next
        while current:
            check = stack.pop()
            if current.val != check.val:
                stack.append(check)
                check.next = current 
            while current and current.val == check.val:
                current = current.next
            if current:
                if stack: stack[-1].next = current 
                stack.append(current)
                current = current.next
        
        if not stack: return None
        stack[-1].next = None
        return stack[0]