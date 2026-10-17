# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        headTwo = head
        count = 0 
        while headTwo.next:
            print(headTwo.val)
            count += 1
            headTwo = headTwo.next
        
        place = count - n

        if place < 0:          # removing the head
            return head.next
            
        curr = head
        prev = None
        for i in range(place + 1):
            prev = curr 
            curr = curr.next

        prev.next = curr.next

        return head