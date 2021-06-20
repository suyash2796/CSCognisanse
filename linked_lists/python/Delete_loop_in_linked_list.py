class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        ptr1 = head
        ptr2 = head
        while ptr2!=None and ptr2.next!=None:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 == ptr2 :
                self.delete_loop(head,ptr1)
        else:
            return 1
        
    def delete_loop(self,head,loop_node):
        ptr1 = head
        i = 1
        counter = loop_node
        while counter.next != loop_node:
            counter = counter.next
            i+=1

        ptr2 = head
        for j in range(i):
            ptr2 = ptr2.next

        while ptr1!=ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        while(ptr2.next != ptr1):
            ptr2 = ptr2.next
            
        ptr2.next = None

        # code here
        # remove the loop without losing any nodes


#{ 
#  Driver Code Starts
# driver code:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,num):
        if self.head is None:
            self.head=Node(num)
            self.tail=self.head
        else:
            self.tail.next=Node(num)
            self.tail=self.tail.next
    
    def isLoop(self):
        if self.head is None:
            return False
        
        fast=self.head.next
        slow=self.head
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast=fast.next.next
            slow=slow.next
        
        return True
    
    def loopHere(self,position):
        if position==0:
            return
        
        walk=self.head
        for _ in range(1,position):
            walk=walk.next
        self.tail.next=walk
    
    def length(self):
        walk=self.head
        ret=0
        while walk:
            ret+=1
            walk=walk.next
        return ret

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=tuple(int(x) for x in input().split())
        pos=int(input())
        
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)
        
        Solution().removeLoop(ll.head)
        
        if ll.isLoop() or ll.length()!=n:
            print(0)
            continue
        else:
            print(1)

# } Driver Code Ends
