class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        t = head
        y = 0
        while t:
            y=y+1
            t = t.next
        n = y-n
        
        dummy = ListNode(0,head)
        head = dummy
        temp = head
        for i in range(n):
            print(i)
            temp = temp.next
        temp.next = temp.next.next
        return head.next
