# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        count = head
        len=1
        while count.next:
            count = count.next
            len += 1
        
        k = k % len
        tail_point = len - k - 1

        tail = head
        
        for i in range(tail_point):
            tail=tail.next
        
        count.next=head
        head=tail.next
        tail.next=None
        return head