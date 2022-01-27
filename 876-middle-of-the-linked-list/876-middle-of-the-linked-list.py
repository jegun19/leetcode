# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = head
        c = 1
        while length.next is not None:
            length = length.next
            c += 1
            
        lim = int(c/2) + 1
        count = 1
        ans = list()
        start = head
        print(lim, start)
        while True:
            if count != lim:
                start = start.next
                count += 1
            else:
                return start
