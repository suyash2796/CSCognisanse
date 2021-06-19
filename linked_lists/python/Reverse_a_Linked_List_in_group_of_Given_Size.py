class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: # Three Pointer method
    def reverse(self,head, k):
        curr = head # Current Node Pointer
        prev = None # Previous Node Pointer
        Next = None # Next Node Pointer
        Count = 0 # keeping track of sub array counts (subarrays are k sized)
        while curr != None and Count<k:
            
            Next = curr.next # Store next node of current in Next)
            curr.next = prev # reversing next node of current from next to previous
            
            prev = curr # changing prev to curr (moving prev pointer ahead)
            curr = Next # changing curr to saved Next (moving curr pointed ahead)
            
            Count+=1 # increasing count and exiting loop when count ==k
            
        if Next is not None: # recursive call for next k elements
            head.next = self.reverse(Next, k)
        
        return prev
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
    head = sol.reverse(a,k=2)
    while head:
      l.append(head.val)
      head = head.next
    print(l)
    
