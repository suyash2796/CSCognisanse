class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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
            temp = temp.next
        temp.next = temp.next.next
        return head.next
    
if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    sol = Solution()
    l = []
    head = sol.removeNthFromEnd(a,n=2)
    while head:
      l.append(head.val)
      head = head.next
    print(l)
    
