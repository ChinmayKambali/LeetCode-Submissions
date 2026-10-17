# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        temp = head
        count = 0 
        while temp:
            count += 1
            temp = temp.next
        
        print(count)
        place = count - n

        if place <= 0:
            return head.next

        curr = head
        prev = None
        for i in range(place):
            prev = curr 
            curr = curr.next

        prev.next = curr.next

        return head