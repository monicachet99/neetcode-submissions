class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head

        c = head
        p = d

        # Move c n steps ahead
        for _ in range(n):
            c = c.next

        # Move both pointers until c reaches the end
        while c:
            c = c.next
            p = p.next

        # Remove the nth node from the end
        p.next = p.next.next

        return d.next