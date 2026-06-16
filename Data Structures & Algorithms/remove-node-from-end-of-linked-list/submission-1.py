class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head

        c = head
        p = d
        k = 0

        while c != None:
            k += 1
            c = c.next

        c = head
        i = 0

        while i < (k - n):
            p = p.next
            i += 1

        p.next = p.next.next

        return d.next